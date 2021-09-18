def disphelp(matrix):
    for i in matrix:
        print(i)
    print("--------------")
def subsetSum(arr , reqsum):
    
    dp = [[1 if i==0 else 0 for i in range(reqsum+1)] for j in range(len(arr)+1)]
    disphelp(dp)
    for i in range(1 , len(dp)):
        for j in range(1 , len(dp[0])):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    disphelp(dp)

subsetSum([1 , 5 , 11 , 5] , 11) 