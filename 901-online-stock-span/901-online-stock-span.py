class StockSpanner:

    def __init__(self):
        
        self.stack=[[0,0]]
        
    #find index of previous smaller elment
        
    def next(self, price: int) -> int:
        
        
        count=1
        
        while(self.stack and price>=self.stack[-1][1] ):
            count+=self.stack.pop()[0]
        
        else:
            self.stack.append([count,price])
        return count        

