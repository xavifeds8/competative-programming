denominations  = [1 , 2, 5 , 10 , 20 , 50 , 100 , 500 , 1000] #this method wont work if the denom[i] + denom[i-1] > denom[i+1]
value = 68
count  = []
for i in range(len(denominations)-1 , -1 , -1):
    while value >= denominations[i]:
        value-=denominations[i]
        count.append(denominations[i])
print(count)
    