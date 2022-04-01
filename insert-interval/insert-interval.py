class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        #0(nlogn) solution adding new interval sorting and then merging
        
        intervals.append(newInterval)
        
        merged=[]
        
        intervals.sort(key=lambda x:x[0])   #sort intervals by start index
        
        
        
        
        for i in (intervals):
                
            if (merged and i[0]<=merged[-1][1]):
            
                merged[-1][1]= max(i[1],merged[-1][1])
                    
            else:
                merged.append(i)
            
        return merged
        
        
        
        
       
    
        
   