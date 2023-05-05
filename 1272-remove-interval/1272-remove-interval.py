class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        
        x1,x2 = toBeRemoved[0],toBeRemoved[-1]
        
        
        res = []
        
        for i in intervals:
            
            start,end =i[0],i[1]
            
            
            if start>x2 or end<x1 :     res.append([start,end])
                
            
            
            else:   
                
                if start<x1:    res.append([start,x1])

                if end >x2:     res.append([x2,end])
                    
                    
                    
        return res