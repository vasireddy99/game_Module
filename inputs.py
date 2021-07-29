from play_sudoku import *
from sudoku_solver import *
from games import *

def user_input():
    print("Enter input '1' or '2' ")

    x = input()
    if x =="1":
        solve_board(game1)

    if x =='2':
        print(game2)

    if x =='3':
        print(game3)

def solve_board(board):
    while True:
        print_board(board)
        #revert(g)
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
            print("input has made sudoku invalid, Please enter the valid inputs again")
            erase(row, col, board)
            solve_board(board)
        print("do you want to select more coordinate, select 'y' or 'n'")
        selection = input()
        if selection =='y':
            continue
        else:
            break
    print("The rest will be solved by bot")
    solve_sudoku(board)
    print(board)