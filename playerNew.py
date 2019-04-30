from random import randint
import datetime, random
import functools
from itertools import product
from abc import ABC, abstractmethod
import collections, os, pickle
from colors import color
import numpy as np
'''
Tictactoe game for ML
Allison Bolen

'''

class BaseAgent(ABC):

    def __init__(self, learning_rate, discount_rate, exploration_rate, exploration_decay):
        '''
        params:
            learning rate
            discount rate
        '''
        self.state_name_dict = {}
        self.LR = learning_rate
        self.DR = discount_rate
        self.ER = exploration_rate
        self.ED = exploration_decay
        #make list of possible actions
        self.actions = list(product([0,1,2],[0,1,2]))
        self.Q = {}
        # initialize all action values to zero
        for action in self.actions:
            self.Q[action] = collections.defaultdict(int)
        #rewards
        self.rewards = []

    def request_action(self, state):
        '''
        give me n action given the current game state
        '''
        valid_actions = self.get_valid_actions(state)
        take_action = None
        rand = random.random()
        if rand < self.ER:
            # explore
            print(color.RED+"Explore action"+color.END)
            take_action = valid_actions[random.randint(0, len(valid_actions)-1)]
        else:
            #exploit
            print(color.PURPLE+"Exploit action"+color.END)
            values = np.array([self.Q[a][state] for a in valid_actions])
            # get max of values
            index_max = np.where(values == np.max(values))[0]
            if len(index_max)  > 1:
                # multiple maxs
                index_selection = np.random.choice(index_max,1)[0]
            else:
                # single max
                index_selection = index_max[0]
            take_action =  valid_actions[index_selection]

        self.ER *= (1.-self.ED)

        return take_action

    def exploit_action(self, state):
        valid_actions = self.get_valid_actions(state)
        take_action = None
        print(color.PURPLE+"Exploit action"+color.END)
        values = np.array([self.Q[a][state] for a in valid_actions])
        # get max of values
        index_max = np.where(values == np.max(values))[0]
        if len(index_max)  > 1:
            # multiple maxs
            index_selection = np.random.choice(index_max,1)[0]
        else:
            # single max
            index_selection = index_max[0]

        take_action = valid_actions[index_selection]
        return take_action

    def random_action(self, state):
        valid_actions = self.get_valid_actions(state)
        take_action = None
        print(color.RED+"Explore action"+color.END)
        take_action = valid_actions[random.randint(0, len(valid_actions)-1)]
        return take_action

    def get_valid_actions(self, state):
        return [a for a in self.actions if state[a[0]*3 + a[1]] == '-']

    def save_it_all(self, obj, filename):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    @abstractmethod
    def learn(self, state, next_state, action, next_action, reward):
        pass

class QLearningAgent(BaseAgent):
    def __init__(self, learning_rate, discount_rate, exploration_rate, exploration_decay=0.):
        super().__init__(learning_rate, discount_rate, exploration_rate, exploration_decay)

    def learn(self, state, next_state, action, next_action, reward):
        if next_state is not None:
            valid_actions = self.get_valid_actions(next_state)
            Q_options = [self.Q[action][next_state] for action in valid_actions]
            # update values at the previous edge
            self.Q[action][state] += self.LR*(reward + self.DR*max(Q_options)-self.Q[action][state])
        else:
            # terminal state,
            self.Q[action][state] += self.LR*(reward - self.Q[action][state])

        self.rewards.append(reward)
