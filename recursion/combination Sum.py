"""
Given an array of integers A[] of size N and a sum B
find all unique combinations in A where the sum is equal to B.
Each number in A may only be used once in the combination.
"""

def comb(arr  , sum_ , target , i):
    if sum(sum_) == target:
        print(sum_)
        return
    if i>= len(arr):
        return 
    if sum(sum_) > target:
        return
    sum_.append(arr[i])
    comb(arr , sum_ , target  , i+1)
    sum_.pop(-1)
    comb(arr , sum_ , target  , i+1)
arr = [9, 1, 2, 7, 6, 1, 5]
arr.sort()
comb(arr , [] , 8 , 0)