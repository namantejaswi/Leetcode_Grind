class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        freq = {}
        
        for c in tasks:
            if c in freq:   freq[c] +=1
                
            else: freq[c] = 1
            
            
        heap = [-f for f in freq.values()]
        
        
        heapq.heapify(heap)
        
        curr_time = 0
        
        dic = {}
        
        
        while dic or heap:
            
            time_delta = curr_time - n - 1
            #the items in our dictionary is eligible to go back if they were added more than time delta back 
            
            if time_delta in dic:
                heapq.heappush(heap,dic.pop(time_delta))
                
            if heap:
                cnt= heapq.heappop(heap)+1
                
                if cnt!= 0:
                    dic[curr_time]=cnt
                    
            curr_time+=1
            
        return curr_time
                    
            
        
        
        
                
                
                
        
        