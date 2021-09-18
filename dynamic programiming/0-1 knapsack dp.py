value = [15 , 14 , 10 , 45 , 30]
weight = [2 , 5 , 1 , 3 , 4]
W = 7
def disp(matrix):
    for i in matrix:
        print(i)
    print("---------")
dp =[[0 for i in range(W+1)] for j in range(len(value)+1)]
for i in range(1 , len(value)+1):
    for j in range(1 , W+1):
        if j-weight[i-1] >= 0:
            dp[i][j] = max(dp[i-1][j] , value[i-1] + dp[i-1][j-weight[i-1]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])