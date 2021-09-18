matrix = [[ 10, 10, 2, 0, 20, 4 ],
        [ 1, 0, 0, 30, 2, 5 ]]
dp = [[-1 for i in range(len(matrix[0]))] for j in range(len(matrix))]
def pathSum(i, j):
    if i>=len(matrix) or j >= len(matrix[0]):
        return -10**9
    if i==len(matrix)-1 and j == len(matrix[0])-1:
        return matrix[-1][-1]
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] =  matrix[i][j] + max(pathSum(i+1 , j) , pathSum(i ,j+1))
    return dp[i][j]
print(pathSum(0 , 0))
