class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        
        
        lo = 1
        hi = totalTrips*max(time)
        
        
        while lo<hi:
            
            mid = (lo+hi)//2
            s=0
            
            for t in time:
                
                s+= mid//t
                
                
            if s>= totalTrips: 
                hi=mid
                
                #print("trips sufficient",lo,hi)
                
            else:   
                lo=mid+1
                #print("trips not sufficient")
                
        #print(lo,mid,hi)      
        return int(lo)