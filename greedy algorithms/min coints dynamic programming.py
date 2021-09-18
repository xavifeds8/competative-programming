denominations = [1 , 5 , 6 , 9 ]
val = int(input())
dp = [10**9 for i in range(val+1)]
dp[0] = 0
for i in range(1 , val+1):
    for j in denominations:
        if i>=j:
            dp[i] = min(dp[i] , dp[i-j]+1)
print(dp)


