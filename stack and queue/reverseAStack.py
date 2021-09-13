stack = [1 ,2,3 ,4 ,5]

def insertAtBottom(stack , item):
    if len(stack)==0:
        stack.append(item)
        return 
    else:
        temp = stack.pop(-1)
        insertAtBottom(stack  , item)
        stack.append(temp)
# insertAtBottom(stack , 6)

def  reverse(stack):
    if len(stack) == 0:
        return 
    else:
        key = stack.pop(-1)
        reverse(stack)
        insertAtBottom(stack , key)
reverse(stack)
print(stack)

