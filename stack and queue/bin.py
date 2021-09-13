n = 5
dp = ["0" for i in range(n)]
dp[1] = "01"
for i in range(2 , len(dp)):
    res = dp[i-1]
    for j in dp[i-1]:
        if j=="0":
            res+="1"
        else:
            res+="0"
    dp[i] = res
print(dp)
