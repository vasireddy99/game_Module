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


def modify_board(x, y, v, board):
    if board[x][y] == 0:
        board[x][y] = v
    else:
        print("value already exists")
        return False
    return True


def user_hint(board):
    i, j = 0, 0
    while i and j:
        i = random.randrange(1, 9)
        j = random.randrange(1, 9)
        if board[i][j] == 0:
            print("The hint for the co-ordinate {} is {}".format('[i][j]', solved_board(i, j)))
            break


def erase(x, y, board):
    if board[x][y] == 0:
        print("The point is already cleared")
    elif board[x][y] != 0:
        board[x][y] = 0
        print("Point is cleared")
    print_board(board)
