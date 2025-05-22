def isSafe(mat, row, col):
    n = len(mat)

    for i in range(col):
        if mat[i][row]:
            return False
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):