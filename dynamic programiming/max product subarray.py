"""
Given an integer array nums, find a contiguous non-empty subarray
within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.


Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

nums = [2 , 3 ,-1, -2 , 4]
posnum = 1
negnum = 1
res = max(nums)
for i in range(len(nums)):
    if nums[i] == 0:
        posnum = 1
        negnum = 1
        continue
    temp = posnum
    posnum = max(negnum*nums[i] , posnum * nums[i] , nums[i])
    negnum = min(negnum*nums[i] , temp * nums[i], nums[i])
    res = max(res , posnum)
print(res)