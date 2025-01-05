class MedianFinder:

    def __init__(self):
        
        self.min_heap=[]
        self.max_heap=[]

    def addNum(self, num: int) -> None:
        
        
        if len(self.max_heap)==0:
             heapq.heappush(self.max_heap,-1*num)
            
        elif(num*-1>=self.max_heap[0]):
            heapq.heappush(self.max_heap,-1*num)

        elif(-1*num<self.max_heap[0]):
            heapq.heappush(self.min_heap,num)
        
        if(len(self.max_heap)-len(self.min_heap)>1):
            
            root=heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-1*root)
        
        
        if(len(self.min_heap)-len(self.max_heap)>1):
            
            r=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-1*r)
        

    def findMedian(self) -> float:
        
        if(len(self.max_heap)==len(self.min_heap)):
            return((-1*self.max_heap[0]+self.min_heap[0])/2)
        
        elif (len(self.max_heap)>len(self.min_heap)):
             return(-1*self.max_heap[0])
             
        else:
             return(self.min_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()