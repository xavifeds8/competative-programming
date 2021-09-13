lst = [2 , 5 , 1 ,8 ,2 ,9 , 1]
k = 3
val =  sum(lst[:k])
max_val =val
for i in range(k , len(lst)):
    val = val + lst[i] - lst[i-k]
    max_val = max(max_val , val)
print(max_val)