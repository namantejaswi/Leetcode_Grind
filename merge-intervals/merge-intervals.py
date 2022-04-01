class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        '''
        An overlapp occurs when the end of one preceding interval is greater than the start of our  
        next or following interval, this to say the starting index of our intervals are in non                 increasing order.   
        
        Thus it would be useful to sort the intervals by their start index!
    
        '''
        result=[]
        s_intervals=sorted(intervals,key=lambda i:i[0])  #i[0] to sort by first index
            
            
        for j in s_intervals:
            if (result and j[0]<=result[-1][1]):#second starts
                
        #if result is not null and start of last interval is less than start of first interval
        #then end of last interval is the greater of the end of 1st and last interval
                result[-1][1] = max(j[1], result[-1][1])
            else:
                result +=[j]
        return result
		