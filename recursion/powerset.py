nums = [2]
def recur(i , n , nums , temp):
    if i < n:
        recur(i+1 , n , nums , temp + [nums[i]])
        recur(i+1 , n , nums , temp)
    else:
        print(temp)
recur(0 , len(nums) , nums , [])