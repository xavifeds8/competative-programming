stack = [51 ,4 ,30 , 2 ,1]

def get_sorted(stack , item):
    if not len(stack) or item > stack[-1]:
        stack.append(item)
        return 
    temp = stack.pop(-1)
    get_sorted(stack , item)
    stack.append(temp)

def Sort(stack):
    if len(stack)==0:
        return 
    temp = stack.pop(-1)
    Sort(stack)
    get_sorted(stack , temp)
Sort(stack)
print(stack)