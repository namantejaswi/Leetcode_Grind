class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        
        
        meetings.sort(key = lambda x:x[0])
        
        res = [0]*(n)
        
        
        ready= [ i for i in range(n)]
        
        in_use=[]

        
        #ready has the index of the rooms which are free to be used
        #in_use has the end time, index as in a heap, earliest ending top of min heap
        
        
        for s,e in meetings:
            
            
            while in_use and in_use[0][0]<=s:
            
    
                t,i = heapq.heappop(in_use)
                #we remove the element from in_use since at this time step the room
                #is no longer in use
                
                heapq.heappush(ready,i)      
                #we add the index of the room to ready
                
            if ready:
                
                #if we have some room available we use the room till the end time e of current task and push it to the in_use heap with end time and index 
                
                i = heapq.heappop(ready)
                heapq.heappush(in_use,[e,i])
                
                
                #if no room is free we delay the task and choose a room from in_use with the earliest end time
        
            else:   
                
                t,i=heapq.heappop(in_use)
                heapq.heappush(in_use,[t+e-s,i])  #add duration e-s to the time
            
            res[i]+=1
            
        return res.index(max(res))