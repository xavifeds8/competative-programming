"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor."""

cost = [1 , 100 , 1 , 1, 1, 100]
dp = [0 for i in range(len(cost)+1)] # dp[i] the minimun cost to reach the postition from 0
dp[1] = cost[0]
for j in range(2 , len(dp)):
    dp[j] = min(dp[j-1] + cost[j-1]  , dp[j-2] + cost[j-2])
print(dp)


#space optimised

curr , prev , prev2 = 0 ,0,0
for i in range(1 , len(cost)):
    jumpOne = prev + cost[i-1]
    jumpTwo = prev2 + cost[i-2]
    curr = min(jumpOne , jumpTwo)
    prev , prev2 = curr , prev
print(curr)


