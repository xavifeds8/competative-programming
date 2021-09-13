def joseph(lst , start , k):
    if len(lst) == 1:
        return lst[0]
    start = (start + k)%len(lst)
    lst.pop(start)
    return joseph(lst , start , k)
n = 5
k  = 2
lst = [i for i in range(1 , n+1)]
print(joseph(lst , 0 , k-1))