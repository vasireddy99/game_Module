from play_sudoku import *
from sudoku_solver import *
from games import *

# def user_input():
#     print("Enter input '1' or '2' ")
#
#     x = input()
#     if x =="1":
#         solve_board(game1)
#
#     if x =='2':
#         print(game2)
#
#     if x =='3':
#         print(game3)

def solve_board(board):
    while True:
        print_board(board)
        revert_board = board
        print("select coordinates ")
        row = int(input("Enter Row: "))
        while row<0 or row >8:
            print("Invalid entry please choose any number between 0 to 9")
            row = int(input("Enter Row: "))
            if 0>=row>=8:
                break

        col = int(input ("Enter Column: "))
        while col<0 or col >8:
            print("Invalid entry please choose any number between 0 to 9")
            col = int(input("Enter Col: "))
            if 0>=col>=8:
                break

        value = int(input("select in between 1 to 9: "))
        while value<1 or value >9:
            print("Invalid entry please choose any number between 1 to 9")
            value = int(input("Enter Value: "))
            if 1>=value<=9:
                break

        if not modify_board(row,col,value,board):
            continue
        if not isValidSudoku(board):
            print("invalid sudoku inputs, Please enter the valid inputs again")
            board = revert_board
            continue
        print("do you want to select more coordinate, select 'y' or 'n'")
        selection = input()
        if selection =='y':
            continue
        else:
            break
    print("The rest will be solved by bot")
    solve_sudoku(board)
    print(board)

def create_board():
    board = [[0 for _ in range(9)]for _ in range(9)]
    return board

def valid_input(value):

    input_ = int(input("Enter {}: ").format(value))

    while input_ < 0 or input_ > 8:
        print("Invalid entry please choose any number between 0 to 9")
        input_ = int(input("Enter {}: ").format(value))
        if 0 >= input_ >= 8:
            break
    return input_

def valid_input_(value):
    input_ = int(input("Enter {}: ").format(value))

    while input_ < 1 or input_ > 9:
        print("Invalid entry please choose any number between 1 to 9")
        input_ = int(input("Enter {}: ").format(value))
        if 1 >= input_ >= 9:
            break
    return input_