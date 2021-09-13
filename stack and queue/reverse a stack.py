stack = [1 ,2 , 3, 4, 5 ,6]

def bottom(stack , val):
    if len(stack)==0:
        stack.append(val)
        return 
    x = stack.pop(-1)
    bottom(stack , val)
    stack.append(x)

def reverse(stack):
    if len(stack)==0:
        return 
    x = stack.pop(-1)
    reverse(stack)
    bottom(stack ,x)
    
reverse(stack)
print(stack)