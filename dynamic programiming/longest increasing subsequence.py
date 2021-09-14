"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by 
deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]."""
nums = [50 , 3 , 10 , 7 , 40 , 80 , 1]
#O(n**2)
def LIS(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = 1
    for i in range(1,len(dp)):
        dp[i] = 1
        for j in range(0 , i):
            if nums[j] < nums[i] :
                dp[i] = max(dp[i] , dp[j]+1)
    return max(dp)

#O(nlogn)
nums = [50 , 3 , 10 , 7 , 40 , 80 , 1]
res = [nums[0]]
def binSearch(i , j , key):
    mid = (j-i)//2 + i
    if j<i:
        return i
    if key > res[mid]:
        return binSearch(mid+1 , j ,key)
    else:
        return binSearch(i , mid-1 ,key)

def binLIS(nums):
    for i in range(1 , len(nums)):
        if res[-1] < nums[i]:
            res.append(nums[i])
        else:
            idx = binSearch(0 , len(res)-1 , nums[i])
            res[idx] = nums[i]
    return len(res)
print(binLIS(nums))


