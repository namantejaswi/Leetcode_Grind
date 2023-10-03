class MinStack:

    def __init__(self):
        
        self.stack = []
        self.mi_till_index = []

    def push(self, val: int) -> None:
        
        self.stack.append(val)
        
        if self.mi_till_index:  self.mi_till_index.append(min(self.mi_till_index[-1],val))
        else:   self.mi_till_index.append(val)
        
    def pop(self) -> None:
        
        self.stack.pop()
        self.mi_till_index.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.mi_till_index[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()