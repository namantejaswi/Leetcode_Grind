class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        intervals.sort(key = lambda x:x[0])
        
        print(intervals)
        
        res=[]
        
        for t in (intervals):
            
            
            #if we have something in result
            #we check that if the start of the second element is less than the end of
            #the previous element in res
            #if so we merge them and put them in the array
            #if not we add them seperately
            
            
            if not res:     res.append(t)
                
            elif res and res[-1][1]>=t[0]:   #end of last larger or equal to cur start 
            
                res[-1][1]=max(t[1],res[-1][1])
                
            else:   res.append(t)
                
        return res