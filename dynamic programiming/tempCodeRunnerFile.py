t = [1 , 100 , 1 , 1, 1, 100]
dp = [0 for i in range(len(cost)+1)] # dp[i] the minimun cost to reach the postition from 0
dp[1] = cost[0]
for j in range(2 , len(dp)):
    dp[j] = 