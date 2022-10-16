class MyCalendar:

    def __init__(self):
        
        
        self.dates=[]

    def book(self, start: int, end: int) -> bool:
        
        for  latest_start,latest_end in self.dates:            
            if latest_start<end and latest_end>start:
                return False
        
        self.dates.append((start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


