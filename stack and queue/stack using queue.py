def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    while len(queue_1):
        queue_2.append(queue_1.pop(0))
    queue_1.append(x)
    while len(queue_2):
        queue_1.append(queue_2.pop(0))
    
    # code here


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    
    # code here
    if len(queue_1) == 0:
        return -1
    else:
        return queue_1.pop(0)