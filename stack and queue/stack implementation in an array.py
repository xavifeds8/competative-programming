class Stack:
    def __init__(self):
        self.stk = []
        pass
    def push(self , data):
        self.stk.append(data)
    def pop(self):
        return self.stk.pop(-1)
    def isEmpty(self):
        if len(self.stk) == 0:
            return True
        return False
    def disp(self):
        print(self.stk)
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(16)
s.pop()
s.disp()
    