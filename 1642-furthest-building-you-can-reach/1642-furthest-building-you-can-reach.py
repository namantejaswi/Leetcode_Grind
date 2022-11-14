class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        
        ladder_used=[]
        
        for i in range(len(heights)-1):
            
            diff=heights[i+1]-heights[i]
                
            if diff>0:
                
                heapq.heappush(ladder_used,diff)
                
                if len(ladder_used)>ladders:
                    
                    #pop the ladder used for lowest difference
                    
                    bricks-=heapq.heappop(ladder_used)
                    
                    if bricks<0:    return i #cant continue beyond i
                    
                    
        return len(heights)-1