class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        
        
        #We explore the lowest delta path first as the length of path is not the
        #thing we are constrained with.
        
        
        heap=[]
        visited=set()
        
        heap.append([heights[0][0],0,0])
        visited.add((0,0))
        
        r=len(heights)
        c=len(heights[0])
        
        mx=0
        
        while heap:
            
            
            node=heapq.heappop(heap)
            
            
            val=node[0]
            x=node[1]
            y=node[2]
            
            #print('delta',node[0],'curr height',node[1],node[2])
            
            if x!=0 or y!=0:mx=max(mx,val)
            visited.add((x,y))
            
            if x==r-1 and y==c-1:   return mx
            
            
            for i,j in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                
                
                if i>=0 and i<r and j>=0 and j<c and (i,j) not in visited:
            
                    heapq.heappush(heap,[abs(heights[x][y]-heights[i][j]),i,j])
                
                    
        
        
        
                
            
    
        
        