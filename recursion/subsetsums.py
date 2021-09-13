s = [3 , 1,2]
def recur(i , n , sum , s):
    if i<n:
        recur(i+1 , n , sum + s[i] , s)
        recur(i+1 , n, sum , s)
    else:print(sum)
recur(0 , len(s) , 0 , s)