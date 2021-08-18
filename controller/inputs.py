from utils.play_sudoku import *
from utils.sudoku_solver import *


# def user_input():
#     print("Please choose 'easy', 'medium' or 'hard' ")
#
#     x = input()
#     if x =="easy":
#         solve_board(game1)
#
#     if x =='medium':
#         print(game2)
#
#     if x =='hard':
#         print(game3)

def solve_board(board):
    sudoku_filled_count = 0
    while True:

        print_board(board)
        revert_board = board
        print("select coordinates ")
        row = valid_row_input()
        col = valid_column_input()
        value = valid_value_input()

        if not modify_board(row, col, value, board):
            continue
        if not isValidSudoku(board):
            print("invalid sudoku inputs, Please enter the valid inputs again")
            board = revert_board
            continue
        sudoku_filled_count += 1
        if sudoku_filled_count > 3:
            print("do you want to select more coordinate, select 'y' or 'n'")
            selection = input()
            if selection == 'y':
                continue
            else:
                break

    print("The rest will be solved by the bot")
    solve_sudoku(board)
    print_board(board)


def create_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board


def valid_row_input():
    try:
        row = int(input("Enter Row: "))
    except ValueError:
        print(" Please input integer")
        valid_row_input()
    if row < 0 or row > 8:
        print("Invalid entry please choose row between 0 to 8")
        valid_row_input()
    elif 0 <= row <= 8:
        return row


def valid_column_input():
    try:
        column = int(input("Enter column: "))
    except ValueError:
        print(" Please input integer")
        valid_column_input()
    if column < 0 or column > 8:
        print("Invalid entry please choose column between 0 to 8")
        valid_column_input()
    elif 0 <= column <= 8:
        return column


def valid_value_input():
    try:
        value = int(input("Enter value between 1 to 9: "))
    except ValueError:
        print(" Please input integer")
        valid_value_input()
    if value < 0 or value > 8:
        print("Invalid entry please choose value between 1 to 9")
        valid_value_input()
    elif 1 <= value <= 9:
        return value

