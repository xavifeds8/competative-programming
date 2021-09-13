class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.Minele = 10**9

    def push(self , x):
        if len(self.stack)==0:
            self.Minele = x
            self.stack.append(x)
        elif x < self.Minele:
            modifiedvalue = 2 * x - self.Minele
            self.Minele = x
            self.stack.append(modifiedvalue)
        else:
            self.stack.append(x)
      
    def pop(self):
        if self.stack[-1] < self.Minele:
           self.Minele =  2 * self.Minele - self.stack.pop(-1)
        else:
            self.stack.pop(-1)
    def min(self):
        return self.Minele
    def Print(self):
        print(self.stack)


stk  = MinStack()
stk.push(5)
stk.push(10)
stk.push(3)
print(stk.min())
stk.push(-11)
stk.push(-25)
stk.pop()
print(stk.min())

