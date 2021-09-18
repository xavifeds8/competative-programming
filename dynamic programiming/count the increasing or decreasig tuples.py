rating = [2,5,3,4,1]
res =  0
for i in range(len(range)):
    leftLow = 0 
    leftGreater = 0 
    rightLow = 0 
    rightGreater = 0
    for j in range(i):
        if rating[j] < rating[i]:
            leftLow+=1
        if rating[j] > rating[i]:
            leftGreater +=1
    for j in range(i , len(rating)):
        if rating[j] < rating[i]:
            rightLow+=1
        if rating[j] > rating[i]:
            rightGreater +=1
    res += rightGreater * leftLow + leftGreater * rightLow
print(res)

