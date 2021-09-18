nums = [-4 , -1 , 0 , 3 , 10]
l = 0 
r = len(nums)-1
out = []
while l <= r:
    if abs(nums[l]) >= abs(nums[r]):
        