def naive(arr): #O(n**2)
    res = [-1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    print(res)
# naive([1 , 3 , 2 , 4])

def nextlarger(arr):
    stack = [arr[-1]]
    res = [-1 for i in range(len(arr))]
    for i in range(len(arr)-2 , -1, -1):
        if arr[i] > stack[-1]:
            while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()
            if len(stack):
                res[i] = stack[-1]
            stack.append(arr[i])
            continue
        res[i] = stack[-1]
        stack.append(arr[i])
    print(res)
nextlarger([1 , 3 , 2 , 4])
        
        
