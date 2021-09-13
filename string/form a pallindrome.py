string = "abasadfb"

dp  = [[-1 for i in range(len(string))] for i in range(len(string))]
def palindrome(string , i , j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i>=j:
        dp[i][j] = 0
        return dp[i][j]
    if string[i] == string[j]:
        dp[i][j] =  palindrome(string , i+1 , j-1)
        return dp[i][j]
    else:
        dp[i][j] =min(palindrome(string , i , j-1) , palindrome(string , i+1 , j))+1
        return dp[i][j]
print(palindrome(string , 0 , len(string)-1))