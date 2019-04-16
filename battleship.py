from random import randint
from numpy import * 

#initialize boards
 board = []
  for x in range(5):
      board.append(["0"]*5)

def print_board(board):
    for row in board:
        print(' '.join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board)
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#ask the user for a guess

for turn in range(4):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Colum: "))

    if guess_row == ship_row == guess_col == ship_col
        print("Congratulations you sunk my Battleship!")
