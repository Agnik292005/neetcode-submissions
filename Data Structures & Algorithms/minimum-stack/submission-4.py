class MinStack:

    def __init__(self):
        self.stack=[]
        self.mstack=[]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.mstack.append(val)
        else:
            self.stack.append(val)
            if(val<=self.mstack[-1]):
                self.mstack.append(val)

    def pop(self) -> None:
        if self.stack:
            t=self.stack.pop()
            if self.mstack[-1]==t:
                self.mstack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mstack[-1]
        
