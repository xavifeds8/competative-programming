"""
Given an array of n positive integers.
 Write a program to find the sum of maximum sum subsequence 
 of the given array such that the integers in the subsequence are sorted in increasing order.
input is {1, 101, 2, 3, 100, 4, 5},
 then output should be 106 (1 + 2 + 3 + 100), if the input array is ,"""
nums = [1, 101, 2, 3, 100, 4, 5]
dp = [0 for i in range(len(nums))]
dp[0] = nums[0]
for i in range(1,len(nums)):
    dp[i] = nums[i]
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i] , dp[j] + nums[i])
print(max(dp))