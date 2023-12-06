class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        
        def dist(x1,y1,x2,y2):
            
            delta_x = abs(x1-x2)
            delta_y = abs(y1-y2)
        
            if delta_x==delta_y:    return delta_x
            
            if delta_x > delta_y:   return delta_y +delta_x -delta_y
            
            else: return delta_x + delta_y-delta_x
                          
        res=0
        for i in range(1,len(points)):
            
            res += dist(points[i-1][0],points[i-1][1],points[i][0],points[i][1])
        return res
    
