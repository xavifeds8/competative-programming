value = [1, 5, 8, 9, 10, 17, 17, 20]
dp = [0 for i in range(len(value)+1)]
dp[1] = value[0]
for i in range(2 , len(dp)):
    for j in range(i):
        if i>=j:
            dp[i] = max(dp[i] , dp[i-j-1] + value[j])
        print(dp)
    print("---------")
print(dp)