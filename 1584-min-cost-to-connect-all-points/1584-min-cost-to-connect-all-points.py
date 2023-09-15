class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        
        
        def dist(x,y):
            return (abs(x[0]-y[0])+abs(x[1]-y[1]))
        
        cost = 0
        
        visited = set()
        
        heap = [(0,0)]  #dist, vertex
        
        while len(visited)<len(points):
            
            w,v = heapq.heappop(heap)
            
            if v in visited:    continue
                
            else:
                
                cost+=w
                visited.add(v)
                
                for i in range(len(points)):
                    
                    if i not in visited:
                        
                        heapq.heappush(heap,(dist(points[i],points[v]),i))  #dist,ve
                                       
        return cost