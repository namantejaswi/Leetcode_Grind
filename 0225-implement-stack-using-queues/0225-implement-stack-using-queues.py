class MyStack:

    def __init__(self):
        
        self.q = deque()
        
    def push(self, x: int) -> None:
        
        self.q.append(x)

    def pop(self) -> int:
        
        last = None
        for i in range(len(self.q)-1):
        
            elem = self.q.popleft()

            self.push(elem)
            
            #instead of appending to the same q we could create a new coppy and then
            #deep coppy the 
            
        last = self.q.popleft()
        return last
        
        

    def top(self) -> int:
        l = len(self.q)
        return self.q[l-1]       #Return the last element in the que

    def empty(self) -> bool:
        
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()