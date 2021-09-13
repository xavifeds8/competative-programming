stack = [1 , 3 , 2 , 6 , 1 ,2 ,6]

def insert(stack , key):
    if len(stack)==0 or stack[-1] < key:
        stack.append(key)
        return 
    x = stack.pop(-1)
    insert(stack , key)
    stack.append(x)


def sortArr(stack):
    if len(stack)<=1:
        return stack
    x =  stack.pop(-1)
    sortArr(stack)
    insert(stack , x)

sortArr(stack)
print(stack)