from inputs import *


def user_choice():
    while True:
        user_input = input("choose either 'solve' or 'play': ")

        if user_input.upper() =="PLAY" or user_input.upper() == "SOLVE":
            print(user_input.upper())
            break
        else:
            print("Please choose either 'solve' or 'play'")
            continue

    if user_input.upper()=="SOLVE":
        board = create_board()
        solve_board(board)
    else:
        print("Please select the board")
        player_input()



if __name__ == "__main__":
    user_choice()