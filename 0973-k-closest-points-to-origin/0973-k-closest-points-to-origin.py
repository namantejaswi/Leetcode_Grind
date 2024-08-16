class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        def dist(x,y):
            
            return math.sqrt(x**2 + y**2)
        
        
        arr = []
        
        for p in points:
            
            heapq.heappush(arr,[dist(p[0],p[1]),p])
        
        
        res = []
        
        for i in range(k):
            
            res.append(heapq.heappop(arr)[1])
            
        return res