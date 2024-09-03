class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
       
    
        # we can attend an event i on any day d where d>= start time and d<=end time
        # Eg [1,2] can be attended on d=1 or d =2      1 or 2
        # Eg[2,3] can be attended on day 2 or day 3    3
        # Eg [3,4] can be attended on day 3 or day 4   4 
        # Eg [1,2] again so we choose opposite          opposite
        
        
        # check what events can start today
        # choose the one which ends earliest so you dont block out schedule unnecessarily
        # we will greedily pick the attendable event each day which ends soonest
        
        
        events.sort(key= lambda x:x[0])
        
        print(events)
        
        num_days=0
        for d in events:
            num_days = max(num_days, d[1])
            
        heap_arr = []
        
        cnt = 0
        idx = 0
        
        # days sorted by earlies finish time
        
        for day in range(1,num_days+1):
            
            while idx<len(events) and events[idx][0] ==day:
                
                #add the end time of event to the min heap
                heapq.heappush(heap_arr,events[idx][1])
                idx+=1
            
            # remove any events which were suppposed to start before today
            
            while heap_arr and heap_arr[0]<day:
                heapq.heappop(heap_arr)
                
                
            if heap_arr:
                
                heapq.heappop(heap_arr)
                cnt+=1
                
                
        return cnt
                
                
                
                

        
        
        
        
        
        
        
                    
                    