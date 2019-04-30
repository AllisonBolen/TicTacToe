'''
Tictactoe game for ML
Allison Bolen

'''

import os, pickle
import functools
from colors import color


'''
Info on tic tac Tictactoe

9 moves per game
5 X and 4 O if we start with X first

'''


class Game():
    def __init__(self, agent, verbose, learn, x_focus, o_focus):
        self.agent = agent # agent
        self.board = self.reset_board() # board
        self.CONTINUING = -1 # not at a terminal state
        self.WON = 1 # win state
        self.DRAW = 0 # draw state
        self.VERBOSE = verbose
        self.learn = learn # are we learning or playing
        self.x_focus = x_focus # X reward
        self.o_focus = o_focus # O reward

    def agentMove(self, action, piece):
        self.board[action[0]][action[1]] = piece

    def game_won(self, board, piece):
        if (((board[0][0] == piece) and (board[0][1] == piece) and (board[0][2] == piece))
        or  ((board[1][0] == piece) and (board[1][1] == piece) and (board[1][2] == piece))
        or  ((board[2][0] == piece) and (board[2][1] == piece) and (board[2][2] == piece))
        or  ((board[0][0] == piece) and (board[1][0] == piece) and (board[2][0] == piece))
        or  ((board[0][1] == piece) and (board[1][1] == piece) and (board[2][1] == piece))
        or  ((board[0][2] == piece) and (board[1][2] == piece) and (board[2][2] == piece))
        or  ((board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece))
        or  ((board[0][2] == piece) and (board[1][1] == piece) and (board[2][0] == piece))):

            return True

        return False

    def game_end(self, board, piece):
        if self.game_won(board, piece):
            # won by piece
            return 1
        elif "-" not in self.get_state_encode(board):
            # draw
            return 0
        return -1 # continue

    def get_state_encode(self, board):
        # encode board state:
        return "".join(str(item) for item in functools.reduce(lambda x,y :x+y ,board))

    def play_game(self, agentO, agentX):
        num_moves = None
        done = None
        piece = None
        self.board = self.reset_board()

        num_moves = 0
        done = False

        while( not done ):
            num_moves = num_moves + 1
            prev_state = self.get_state_encode(self.board)
            if num_moves % 2 :
                print(prev_state)

                piece = "X"
                prev_action = agentX.exploit_action(prev_state)
                self.agentMove(prev_action, piece)
            else:
                piece = "O"
                prev_action = agentO.exploit_action(prev_state)
                self.agentMove(prev_action, piece)

            if not self.VERBOSE:
                self.print_board(self.board)

            game_state = self.game_end(self.board, piece)

            if not game_state == self.CONTINUING:
                done = True
                if self.VERBOSE:
                    print("Game over!")
                if game_state == self.DRAW:
                    if self.VERBOSE:
                        print(color.YELLOW+"DRAW"+color.END)
                if game_state == self.WON:
                    if self.VERBOSE:
                        print(color.GREEN+"Won: "+ piece+color.END)
                print("\n")
                return game_state, piece

    def learn_game(self):
        num_moves = None
        done = None
        piece = None
        self.board = self.reset_board()

        prev_state = self.get_state_encode(self.board)
        # prev_action = self.agent.request_action(prev_state)

        num_moves = 0
        done = False

        while( not done ):
            num_moves = num_moves + 1

            if num_moves % 2 :
                piece = "X"
                prev_action = self.agent.random_action(prev_state)
                self.agentMove(prev_action, piece)
            else:
                piece = "O"
                prev_action = self.agent.random_action(prev_state)
                # prev_action = self.agent.request_action(prev_state)
                self.agentMove(prev_action, piece)

            if not self.VERBOSE:
                self.print_board(self.board)

            game_state = self.game_end(self.board, piece)

            if not game_state == self.CONTINUING:
                done = True
                if self.VERBOSE:
                    print("Game over!")
                if game_state == self.DRAW:
                    if self.VERBOSE:
                        print(color.YELLOW+"DRAW"+color.END)
                    reward = 7000
                if game_state == self.WON:
                    if self.VERBOSE:
                        print(color.GREEN+"Won: "+ piece+color.END)
                    if piece == "X":
                        reward = self.x_focus
                    if piece == "O":
                        reward = self.o_focus
                # do final update
                self.agent.learn(prev_state, None, prev_action, None, reward)
                print("\n")
                return game_state, piece
            else:
                reward = 10
            # continuing the game to the next step
            new_state = self.get_state_encode(self.board)

            # dertermin new action
            new_action = self.agent.request_action(new_state)
            #update reward for this situation
            self.agent.learn(prev_state, new_state, prev_action, new_action, reward)
            # reset prev vals
            prev_state = new_state
            prev_action = new_action


    def reset_board(self):
        board = []
        for row in range(0, 3):
            board.append(["-","-","-"])
        return  board

    def print_board(self, board):
        for row in range(0, len(board)):
            print(board[row])
        print()


if __name__ == "__main__":
    main()
