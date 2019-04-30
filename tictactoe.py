'''
Tictactoe game for ML
Allison Bolen

'''

import player
import os, pickle

'''
Info on tic tac Tictactoe

9 moves per game
5 X and 4 O if we start with X first

'''




# globals
GAMES = 1000000
EMPTY = "-"
VERBOSE = False



game_player = player.Player()

def playgame():
    i = None
    num_moves = None
    done = None
    piece = None

    xCount = 0
    oCount = 0
    dCount = 0

    for i in range(0, GAMES):
        print("Game: " + str(i))
        board = reset_board()
        num_moves = 0
        done = False

        while( not done and num_moves < 9 ):
            num_moves = num_moves + 1

            if num_moves % 2 :
                piece = "X"
                board = game_player.doMoveX(board)
            else:
                piece = "O"
                board = game_player.doMoveO(board)

            if VERBOSE:
                print_board(board)

            if game_won(board, piece):
                if VERBOSE:
                    print("Game over. " + piece +" wins!")
                done = True
                if piece == "X":
                    xCount = xCount + 1
                if piece == "O":
                    oCount = oCount + 1
        if num_moves == 9 and not done:
            if VERBOSE:
                print("Draw.")
            dCount = dCount + 1

    print("X: "+ str(xCount) + "!")
    print("O: "+ str(oCount) + "!")
    print("Draw: "+ str(dCount) +"!")


def reset_board():
    board = []
    for row in range(0, 3):
        board.append(["-","-","-"])
    return  board

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

def print_board(board):
    for row in range(0, len(board)):
        print(board[row])
    print()

def load_objects(file):
    with open(file, 'rb') as input:
        return pickle.load(input)

def save_it_all(obj, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    playgame()
