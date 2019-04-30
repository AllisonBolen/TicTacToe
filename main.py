from tictactoeNew import Game
from playerNew import QLearningAgent
from colors import color
import os, pickle

'''
Tictactoe game for ML
Allison Bolen

'''

# the agent was dificult for me to figure out but I referenced some code from https://github.com/rfeinman/tictactoe-reinforcement-learning to get started

'''
This plays all the games or has agents learn the game based on a mode value

If its set to play we load in specified agents and have them play the game
if it is set to learn mode then we have the agent learn given the set rates and rewards

'''

def main():
    i = None
    num_moves = None
    done = None
    piece = None
    GAMES = 200000
    xCount = 0
    oCount = 0
    dCount = 0
    mode = "play" # "learn"
    game = None
    agentO = None
    agentX = None

    if mode == "play":
        agentO = load_objects("./agentORandom.pkl")
        agentX = load_objects("./agentX3.pkl")
        game = Game(None, True, None, None, None)
    else:
        # learn
        agent = QLearningAgent(0.6,0.5,0.9,0.00000099)
        game = Game(agent, True, True, -9000, 10000)

    for i in range(0, GAMES):
        print(color.BOLD+color.CYAN+"Game: "+ str(i+1)+color.END)
        state = None
        player = None
        if mode == "play":
            state, player = game.play_game(agentO, agentX)
        else:
            state, player = game.learn_game()

        if state == 1:
            if player == "X":
                xCount = xCount + 1
            if player == "O":
                oCount = oCount + 1
        else:
            dCount = dCount + 1

    print("X: "+ str(xCount) + "!")
    print("X%: "+ str(xCount/GAMES) + "!")
    print("O: "+ str(oCount) + "!")
    print("O%: "+ str(oCount/GAMES) + "!")
    print("Draw: "+ str(dCount) +"!")
    print("Draw%: "+ str(dCount/GAMES) +"!")

    if mode == "learn":
        agent.save_it_all(agent, "./agentORandom.pkl")

def load_objects(file):
    with open(file, 'rb') as input:
        return pickle.load(input)

if __name__ == "__main__":
    main()
