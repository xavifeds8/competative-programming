matrix) and j == len(matrix[0]):
        return -10**9
    if i==len(matrix)-1 and j == len(matrix)-1:
        return matrix[-1][-1]
    return matrix[i][j] + max(p