#find subarrays with atmost k 1's in it 
nums = [0 , 2 , 0 ,3]
k = 1
i , res = 0 , 0
for j in range(len(nums)):
    k-=nums[j]==1
    while k < 0:
        k+=nums[i] == 1
        i+=1
    res += j-i+1
print(res)
    

