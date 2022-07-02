class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        for i in range(len(capacity)):
            capacity[i]-=rocks[i]
            
        count=0
        
        capacity.sort()
    
        for i in range(len(capacity)):
           
                
            if capacity[i]>additionalRocks:
                capacity[i]-=additionalRocks
                additionalRocks=0
                break
                
            else:   
                
                additionalRocks-=capacity[i]
                capacity[i]=0    
    
    
        for i in range(len(capacity)):
            if capacity[i]==0:
                count+=1
       
        return count
                
    