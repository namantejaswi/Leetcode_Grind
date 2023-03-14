class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pos_speed = list(zip(position,speed))
        
        pos_speed.sort()
            
        
        #time to reach target
        time=[]
        
        for elem in pos_speed:
            
            time.append((target-elem[0])/elem[1])
                    
        curr_time=0
        cnt=0
        
        
        #time is already sorted
        
        #now we sorted the pos_speed array by lowest position and lowet speed so the cars at first are further away and have a change of catchinng up a slower car which is further ahead, since we sorted by position and used speed only as a tie breakker
        
        
        #so we iterate time right to left and see if we can find a smaaller time than current time on the left if so they will form a fleet
        
        for t in reversed(time):
            
            if t>curr_time:     #if we find an elment to the left that takes more time
                                #then we form a fleet i.e cnt+=1
                                
                curr_time=t
                cnt+=1
                
        return cnt
        
        
         
        