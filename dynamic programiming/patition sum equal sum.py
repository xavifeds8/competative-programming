lst = [1 , 5 , 6 , 5]

def partitionSum(arr , sum , req , i):
    if sum == req:
        print(arr)
        return True
    if i>= len(lst):
        return False
    arr.append(lst[i])
    inc = partitionSum(arr , sum + lst[i] , req , i+1)
    arr.pop(-1)
    exc = partitionSum(arr , sum , req , i+1)
    return inc or exc
print("false") if sum(lst)%2 else print(partitionSum([] , 0 , sum(lst)//2 , 0))