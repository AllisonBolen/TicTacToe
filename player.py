from random import randint
import datetime, random
import functools

class Player:

    def __init__(self):
        self.move = None
        self.state_name_dict = {}

    def get_possible_states(self, state_dict, board):
        # encode board state:
        curr_state = "".join(str(item) for item in functools.reduce(lambda x,y :x+y ,board))
        if curr_state not in state_dict:
            state_dict[curr_state] = len(state_dict)

        return state_dict

    def get_state_value(self, state):
        return state_name_dict.get(state,0.0)



    def doMoveO(self, board):
        random.seed(datetime.datetime.now())
        condition = True
        self.state_name_dict = self.get_possible_states(self.state_name_dict, board)

        while condition:
            x = randint(0, 2)
            y = randint(0, 2)
            condition =  board[x][y] != "-"

        board[x][y] = "O"
        return board

    def doMoveX(self, board):
        random.seed(datetime.datetime.now())
        condition = True
        self.state_name_dict = self.get_possible_states(self.state_name_dict, board)
        while condition:
            x = randint(0, 2)
            y = randint(0, 2)
            condition =  board[x][y] != "-"
        board[x][y] = "X"
        return board

    def game_won(board, piece):
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
