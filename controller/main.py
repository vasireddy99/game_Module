from inputs import *

def user_choice():
    user_input = input("choose either play or solve :")
    if user_input =='play':
        print('you chose to play, select the board')
        user_input()

    if user_input == 'solve':
        print('You chose to solve, Please provide the board')
        board = create_board()
        solve_board(board)

if __name__ == "__main__":
    user_choice()