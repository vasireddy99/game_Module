
def sudoku_solver(board):
    subm = [[0] * 3 for _ in range(3)]
    row, col, l = [0] * 9, [0] * 9, []
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
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
                board[i][j] = int(m)
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
