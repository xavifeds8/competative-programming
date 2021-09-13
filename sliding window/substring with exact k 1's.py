nums = [1 , 0 , 1 , 1 , 3, 6 ,5]
def atmost(k):
    i = res = 0
    for j in range(len(nums)):
        k-=nums[j] == 1
        while k<0:
            k+=nums[i] == 1
            i+=1
        res += j-i+1
    return res
n = int(input("enter the value of k\n"))
print(atmost(n)-atmost(n-1))