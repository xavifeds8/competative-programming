stack = [1 , 2, 3,4 , 5, 6]
def bottominsert(stack , val):
    if len(stack)==0:
        stack.append(val)
        return
    x = stack.pop(-1)
    bottominsert(stack , val)
    stack.append(x)
bottominsert(stack , 8)
print(stack)

