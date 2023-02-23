class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        #the least capacity has to be atleast as big as the biggest package
        #now we can hypothetically say that the max capacity can be the total sum in case we want to ship them all at once
        # so essentially we have to apply binary search to find the optimum capacity
        

        
        def can_work ( capacity):
            
            d=1
            curr_sum=0
            for  w in weights:
            
                curr_sum+=w
                
                if curr_sum > capacity:
                    d+=1
                    curr_sum = w #if we ship the next day then curren capacity = w
                    
            return d<=days
            
        
        lo = max(weights)
        hi = sum(weights)
        
        
        while hi>lo:

            mid = (lo+hi)//2
            
            if can_work(mid):
                
                print("works with mid",mid,"high is",hi,"low is",lo)   
                hi = mid
               
            
            else:   
                print(lo,"failed here")
                lo = mid + 1
                print("updated to",lo,hi)
                
        return hi
        
                
                
                
                
                
        
        
        
        
        
        