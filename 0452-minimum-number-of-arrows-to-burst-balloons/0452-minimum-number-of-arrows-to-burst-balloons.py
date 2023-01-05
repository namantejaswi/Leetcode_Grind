class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        
        
        #sort by end 
        # if end of current greater than start next then we dont need another arrow
        # else if start of next greater than end of curr then cnt++
        
        
        
        cnt=1
        
        points =sorted(points, key=lambda x:x[1])
                
        max_reach=points[0][1]
        
        
        for i in range (1,len(points)):
            
            
           # print(points[i][0],points[i-1][1])
            if points[i][0]>max_reach:
                
                cnt+=1
                max_reach=points[i][1]
                
        return cnt
            