"""
Given an array arr[] of size N and an integer K.
Find the maximum for each and 
every contiguous subarray of size K.
"""
nums = [1 , 3 , -1 , -3 , 5 , 3 , 6 , 7]
k = 3
queue = []
res = []
for i in range(len(nums)):
    if i>=k and  queue[0] == nums[i-k]:
        queue.pop(0)
    while len(queue) and queue[-1] < nums[i]:
        queue.pop(-1)
    queue.append(nums[i])
    if i>=k-1:
        res.append(queue[0])
print(res)
