string = "abaabca"

dp = [[1 if i==j else 0 for i in range(len(string))] for j in range(len(string))]
res = 0
def disp(matrix):
    for i in matrix:
        print(i)
    print("------")
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        dp[i][i+1] = 1
disp(dp)

for i in range(len(dp)):
    for j in range(i+2 , len(dp)):
        if string[i] == string[j] and dp[i+1][j-1] ==1:
            dp[i][j] = 1
            res = max(res , j-i+1)
disp(dp)
print(res)
