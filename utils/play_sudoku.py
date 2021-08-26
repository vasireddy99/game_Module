from random import random


def isValidSudoku(board):
    N = 9

    # Use hash set to record the status
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for r in range(N):
        for c in range(N):
            val = board[r][c]
            # Check if the position is filled with number
            if val == 0:
                continue

            # Check the row
            if val in rows[r]:
                return False
            rows[r].add(val)

            # Check the column
            if val in cols[c]:
                return False
            cols[c].add(val)

            # Check the box
            idx = (r // 3) * 3 + c // 3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)

    return True


def print_board(game):
    for i in game:
        print(i)


def modify_board(row, col, val, board):
    if board[row][col] == 0:
        board[row][col] = val
    else:
        print("value already exists")
        return False
    return True


def user_hint(board):
    i, j = 0, 0
    while board[i][j] != 0:
        i = random.randrange(1, 9)
        j = random.randrange(1, 9)
    print("The hint for the co-ordinate {} is {}".format('[i][j]', solved_board(i, j)))


def erase(x, y, board):
    if board[x][y] == 0:
        print("The point is already cleared")
    elif board[x][y] != 0:
        board[x][y] = 0
        print("Point is cleared")
    print_board(board)


def create_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board


def valid_row_input():
    try:
        row = int(input("Enter Row: "))
    except ValueError:
        print(" Please input integer")
        return valid_row_input()
    if row < 0 or row > 8:
        print("Invalid entry please choose row between 0 to 8")
        return valid_row_input()
    elif 0 <= row <= 8:
        return row


def valid_column_input():
    try:
        column = int(input("Enter column: "))
    except ValueError:
        print(" Please input integer")
        return valid_column_input()
    if column < 0 or column > 8:
        print("Invalid entry please choose column between 0 to 8")
        return valid_column_input()
    elif 0 <= column <= 8:
        return column


def valid_value_input():
    try:
        value = int(input("Enter value between 1 to 9: "))
    except ValueError:
        print(" Please input integer")
        return valid_value_input()
    else:
        if value < 1 or value > 9:
            print("Invalid entry please choose value between 1 to 9")
            return valid_value_input()
        elif 1 <= value <= 9:
            return value


def valid_selection_input():
    while True:
        selection = input("Select 'y' or 'n' : ")
        if selection.upper() == "Y" or selection.upper() == "N":
            break
        else:
            continue
    if selection.upper() == "Y":
        return True
    else:
        return False


def board_full(board):
    if 0 in board:
        return True
    else:
        return False


def caluclate_score(start_time, end_time):
    score = 0
    player_time = end_time - start_time
    if player_time < 10:
        score = 10
    elif player_time > 10:
        score = 7
    elif player_time > 20:
        score = 5
    return score
