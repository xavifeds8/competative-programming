def mergeWithoutExtraSpace(arr1 , arr2): #merges the subproblem without extra space
    return sorted(arr1 +  arr2)
    

def partition(nums): #partition the array into halves
    m = (len(nums)-1)//2
    lhalf = nums[:m+1]
    rhalf = nums[m:]
    return mergeWithoutExtraSpace(lhalf  , rhalf)
nums = [1  , 0, 0 ,0,0 ,-1 , -2 ,-199 , 4 , -4]
print(partition(nums))