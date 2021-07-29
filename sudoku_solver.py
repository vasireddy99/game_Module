'''
def solve_sudoku(board):
    # we first check if all the cells are already filled. If yes, that means all cells have been filled by the algorithm and we can return True.
    allFilled = True
    unfilledRow, unfilledCol = -1, -1
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == "0":
                allFilled = False
                unfilledRow, unfilledCol = i, j
                break
        if allFilled == False:
            break
    if allFilled == True:
        return True
    # we create a set of numbers that we have seen in the same row, column, and box
    seenNumbers = set()
    for i in range(0, 9):
        if board[unfilledRow][i] != "0":
            seenNumbers.add(board[unfilledRow][i])
        if board[i][unfilledCol] != "0":
            seenNumbers.add(board[i][unfilledCol])
    for i in range(int(unfilledRow / 3) * 3, int(unfilledRow / 3) * 3 + 3):
        for j in range(int(unfilledCol / 3) * 3, int(unfilledCol / 3) * 3 + 3):
            if board[i][j] != "0":
                seenNumbers.add(board[i][j])
    print(board)
    # we create a set of numbers which can be used as potential candidates for the cell to be filled.
    possibleNums = set()
    for i in range(1, 10):
        possibleNums.add(str(i))
    possibleNums -= seenNumbers
    for num in possibleNums:
        board[unfilledRow][unfilledCol] = num
        # if the chosen num solves the puzzle, return True
        if isValidSudoku(board):
            return True
        # if the chosen num does not solve the puzzle, clear that cell.
        else:
            board[unfilledRow][unfilledCol] = "0"
    # if no potential candidates could solve the puzzle, return False.
    return False
'''


def solve_sudoku(board):
    subm = [[0] * 3 for _ in range(3)]
    row, col, l = [0] * 9, [0] * 9, []
    for i in range(9):
        for j in range(9):
            if board[i][j] != "0":
                row[i] ^= 1 << int(board[i][j])
                col[j] ^= 1 << int(board[i][j])
                subm[i // 3][j // 3] ^= 1 << int(board[i][j])
            else:
                board[i][j] = 0  # we do so that we know we have to place a number at this

    def work(row, col, subm, i, j):
        if i == 9 and j == 0:
            l.append(0)
            return
        if int(board[i][j]) != 0:
            if j == 8:
                work(row, col, subm, i + 1, 0)
                return
            else:
                work(row, col, subm, i, j + 1)
                return
        for m in range(1, 10):
            if (row[i] & (1 << m) == 0) and (col[j] & (1 << m) == 0) and (subm[i // 3][j // 3] & (1 << m) == 0):
                row[i] ^= 1 << m
                col[j] ^= 1 << m
                subm[i // 3][j // 3] ^= 1 << m
                board[i][j] = str(m)
                if j == 8:
                    work(row, col, subm, i + 1, 0)
                else:
                    work(row, col, subm, i, j + 1)
                if len(l) > 0: return  # we found the answer
                row[i] ^= 1 << m
                col[j] ^= 1 << m
                subm[i // 3][j // 3] ^= 1 << m
                board[i][j] = 0

    work(row, col, subm, 0, 0)
    return board
