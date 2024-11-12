class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        
        
        
        intervals.append(newInterval)
        
        merged=[]
        
        intervals.sort(key=lambda x:x[0]) 
        
        
        for i in (intervals):
                
            if (merged and i[0]<=merged[-1][1]):
            
                merged[-1][1]= max(i[1],merged[-1][1])
                    
            else:
                merged.append(i)
            
        return merged