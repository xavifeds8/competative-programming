start = [1 , 3 , 0 , 5 , 8 , 5]
end =  [2 , 4 , 6 , 7 , 9 ,9]
lst = []
for i in range(len(start)):
    lst.append([start[i] , end[i] , i+1])
lst = sorted(lst , key = lambda x:x[1])
val = [lst[0][-1]]
ptr = 0
for i in range(1 , len(start)):
    if lst[i][0] > lst[ptr][1]:
        val.append(lst[i][-1])
        ptr = i
print(val)


