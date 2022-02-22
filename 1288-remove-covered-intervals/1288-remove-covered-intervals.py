class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        
        count=0
        #sort intervals by start for tie breaker take larger interval first
        intervals.sort(key=lambda x:(x[0],-x[1]))
        
        end=0
        #print(intervals)
        
        #A compete overlap will occur only when the end point of a previous interval
        #is greater than the end point of current interval or conversely if the
        #number of non covered intervals increase if current end is greaterthan previous end
        
        for i in range(len(intervals)):
                       
            if intervals[i][-1]>end:
                
                #print(intervals[i][-1],end)
                count+=1
                end=intervals[i][-1]
                
                
        #Edge case when interval start at same index and end at different
        #Sort equal cases by end index
                
        return count
                
                
            