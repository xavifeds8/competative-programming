# """
# Given a string S, find length of the 
# longest substring with all distinct characters. 
# S = "geeksforgeeks"
# Output: 7
# Explanation: "eksforg" is the longest 
# substring with all distinct characters.
# """

S = "geeksforgeeks"
i , j = 0 , 0 
d = {} # lets the index of ist last  occurence in the window
res = 0
for j in range(len(S)):
    if S[j] in d and d[S[j]] >= i:
        i = d[S[j]] + 1
        print(i , j)
    d[S[j]] = j
    if j-i+1 > res:
        s = i
        e = j
        res = max(res , j-i+1)
return res
