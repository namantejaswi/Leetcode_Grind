class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        
        
        time = []
        
        for i in range(len(dist)):
            
            time.append(dist[i]/speed[i])
            
                    
    
        time.sort()
        cnt=0
        curr_time=0
    
        for i in range(len(time)):
            
            if time[i]>i:
                cnt+=1
                
            else:   break
                
        return cnt
        
        
        