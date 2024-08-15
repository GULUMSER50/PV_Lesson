"""Fully working representation of the board (list of lists, other): 2
Correct gravity check (finding the lowest spot in the column): 4
Correct positioning of the piece: 1
Check winner (horizontal): 1
Check winner (vertical): 1
Check winner (diagonal top-right): 1
Check winner (diagonal top-left): 1
Program terminates as soon a player wins: 2"""

from constants import board, board_length, check_winner, step
import os


def read_connect(path):
    path = os.getcwd() + "/connect.txt"
    moves = []
    try:
        with open(path, "r") as file:
            for line in file:
                (player, column) = line.split()
                moves.append((player, int(column)))
    except Exception as e:
        print("Error reading file", e)
    return moves

#moves_list = read_connect("connect.txt")

def check_winner():
    moves = read_connect("connect.txt")
    for idx in moves:
        if list(idx)[0] == 'G1':
            board[int(list(idx)[1])].append('X')
        elif list(idx)[0] == 'G2':
            board[int(list(idx)[1])].append('O')
    return board

def replace_empty_places():
    for i in range(board_length):
        if len(board[i]) < board_length:
            missing = board_length - len(board[i])
            board[i] += missing*'-'
    return board

def check_winner_horizontal(board, board_length):
    check_winner = False
    while not check_winner:
        try:
            for i in range(board_length):
                for j in range(board_length):
                    try:
                        if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] != '-':
                            print("You have won!", board[i][j], board[i][j+1], board[i][j+2], board[i][j+3])
                            check_winner = True

                    except IndexError as e:
                        print("No winner yet!", e)
                        check_winner = True
        except OSError as e:
            exit("No winner yet!",e)



def check_winner_vertical(board, board_length):
    check_winner = False
    while not check_winner:
        try:
            for i in range(board_length):
                for j in range(board_length):
                    try:
                        if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] != '-' :
                            print("You have won!", board[i][j], board[i+1][j], board[i+2][j], board[i+3][j])
                            check_winner = True
                            break
                    except IndexError as e:
                        print("No winner yet!", e)
                        check_winner = False
        except OSError as e:
            exit(e)
            print("No winner yet!", e)
            check_winner = False


def check_winner_diagonal_top_right(board, board_length):
    check_winner = False
    while not check_winner:
        try:
            for i in range(board_length-4):
                for j in range(board_length-4):
                        if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] != '-':
                            print("You have won!", board[i][j], board[i+1][j+1], board[i+2][j+2], board[i+3][j+3])
                            check_winner = True
        except OSError as e:
            exit(f"No winner yet! çünkü {e} oldu.")

board[7][6]
def main():
    board = check_winner()
    check_winner_horizontal(board, board_length)
    check_winner_vertical(board, board_length)
    check_winner_diagonal_top_right(board, board_length)

    return


if __name__ == "__main__":
    print("Game is starting...")
    main()








