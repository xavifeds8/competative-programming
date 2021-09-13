def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    #code here
    while len(stack1):
        stack2.append(stack1.pop(-1))
    stack1.append(x)
    while len(stack2):
        stack1.append(stack2.pop(-1))
    

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    #code herer
    if len(stack1) == 0:
        return -1
    return stack1.pop(-1)