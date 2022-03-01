"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
"""

class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        
        heap=[]
        
        for i in schedule:
            
            for t in i:
                        
                heap.append([t.start,t.end])
        
        heapify(heap)
        
        print(heap)
        val=heapq.heappop(heap)
        start=val[0]
        end=val[1]
        
        #time after which we are free
        free=end
        free_interval=[]
        
        while len(heap)>0:
            
            time=heapq.heappop(heap)
            start=time[0]
            end=time[1]
            
            
            if start>free:
                #object of type interval
                free_interval.append(Interval(free,start))
                free=end
            
            free=max(free,end)
            
        return free_interval
        
    
        
        
        