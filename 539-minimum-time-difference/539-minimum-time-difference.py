class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for i in range(len( timePoints)):
            
            timePoints[i]=(int(timePoints[i][0])*10+int(timePoints[i][1]))*60 + int(timePoints[i][3])*10 +int(timePoints[i][4]) 
        
        
       
        timePoints.sort()
        #print(timePoints)
        
        lowest= timePoints[0]
        highest=timePoints[-1]
    
        
        mi=1441
        delta=float('inf')
        for i in range(1,len(timePoints)):
            
            delta= abs(timePoints[i-1]-timePoints[i])
            
            if delta>720:
                delta=abs(1440-max(timePoints[i-1],timePoints[i]))+min((timePoints[i-1],timePoints[i]))
            
            mi = min(mi,delta)
            
            
        d=abs((1440-highest)+lowest)
                
        return min(mi, d)
                