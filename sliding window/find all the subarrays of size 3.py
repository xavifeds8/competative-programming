arr = [2 , 3, 5 ,2 ,9 ,7]
k = int(input())
lst = []
res =[]
for i in range(len(arr)):
    if i<k:
        lst.append(arr[i])
    else:
        lst.append(arr[i])
        lst.pop(0)
        res+=lst
        
print(res)