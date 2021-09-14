string1 = "xavier"
string2 = "air"
dp = [[-1 for i in range(len(string2))] for j in range(len(string1))]
def LCS_Top_Down(string1 , string2 , i , j):
    if i==len(string1) or j==len(string2):
        return 0
    if dp[i][j]!= -1:
        return dp[i][j]
    if len(string2)==0 or len(string1) == 0:
        return 0
    if string1[i] == string2[j]:
        dp[i][j] = 1+ LCS_Top_Down(string1 , string2 , i+1 , j+1)
        return dp[i][j]
    dp[i][j] = max(LCS_Top_Down(string1 ,string2 , i+1 , j) , LCS_Top_Down(string1 , string2 , i , j+1))
    return dp[i][j]
print(LCS_Top_Down(string1 , string2 , 0 , 0))


