"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product."""

# Input: nums = [1,-2,-3,4]
# Output: 4
# Explanation: The array nums already has a positive product of 24.

nums = [1 , -2 , -3 , 4]
dppos = [0 for i in range(len(nums))]
if nums[0] > 0:
    dppos[0] = 1
dpneg = [0 for i in range(len(nums))]
if nums[0] < 0:
    dpneg[0] = 1
for i in range(len(nums)):
    if nums[i] == 0:
        dppos[i] = dpneg[i] = 0
    if nums[i] > 0:
        dppos[i] = dppos[i-1] + 1
        dpneg[i] = dpneg[i-1] + 1 if dpneg[i-1] !=0 else 0 
    else:
        dpneg[i] = dppos[i-1] +1 
        dppos[i] = dpneg[i-1] + 1 if dpneg[i-1] != 0 else 0  
print(dppos)
print(dpneg)