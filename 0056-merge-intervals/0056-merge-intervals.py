class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        merged = []
        
        intervals.sort(key = lambda x:x[0])
        
        
        
        for i in intervals:
            
            
            if merged and merged[-1][1]>=i[0]:
                
                #upate end to max of start or end overlap
                merged[-1][-1]=max(merged[-1][1],i[1])
            
            else:   merged.append(i)
                
                
        return merged
        
        
        