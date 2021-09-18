"""
You are given N identical eggs and you have access to a K-floored building from 1 to K.

There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break. There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
Return the minimum number of moves that you need to determine with certainty what the value of f is."""

#base cases 
# if numEggs = 0 , res = 10**9
# if numEggs = 1 , res = number of floors
# if numFloor = 0 , res = 0
# if numFloor = 1 , res = 1

floor = 7
eggs = 3

dp = [[0 for i in range(floor+1)] for j in range(eggs+1)]
def disp(matrix):
    for i in matrix:
        print(i)
    print("--------------")
for e in range(len(dp)):
    for f in range(len(dp[0])):
        if e == 0:
            dp[e][f] = 10**2
        elif e == 1:
            dp[e][f] = f
        elif f == 0:
            dp[e][f] = 0
        elif f==1:
            dp[e][f] = 1
        else:
            dp[e][f] = min(dp[e][f] , max(dp[e-1][f-1] , dp[e][floor-f]))+1

 
disp(dp)
