arr = [3 , 4  , 5 , 2]
sum = 6
def subArrSum(i , sum , res , string):
    if sum==res:
        print(string)
        return 
    if i>=len(arr):
        return 
    subArrSum(i+1 , sum , res+arr[i] , string + str(arr[i]) + "->")
    subArrSum(i+1 , sum , res , string)

def disp(matrix):
    for i in matrix:
        print(i)
    print("------------")
def subsetSumDP(arr , sum):
    dp = [[1 if i==0 else 0 for i in range(sum+1)] for j in range(len(arr)+1)]
    for i in range(1 , len(dp)):
        for j in range(1 ,len(dp[0])):
            if dp[i-1][j] == 1:
                dp[i][j] = 1
            elif arr[i-1] <=j and dp[i-1][j-arr[i-1]] == 1:
                dp[i][j] = 1
    disp(dp)
    return dp[-1][-1]

print(subsetSumDP(arr , sum))