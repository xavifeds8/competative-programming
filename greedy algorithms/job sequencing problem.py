Jobs = [(1,4,20),(2,5,60),(3,6,70),(4,6,65),(5,4,25),(6,2,80),(7,2,10),(8,2,22)]
Jobs = sorted(Jobs , key = lambda x:x[2] , reverse= True)
print(Jobs)
count_max_deadline = 0
for i in Jobs:
    count_max_deadline = max(count_max_deadline , i[1])
workDone = [0 for i in range(count_max_deadline+1)]
merePaise = [0 for i in range(count_max_deadline+1)]
for i in Jobs:
    for j in range(i[1] , 0 , -1):
        if workDone[j] == 0:
            workDone[j] = i[0]
            merePaise[j] = i[2]
            break

print(workDone)
print(merePaise)