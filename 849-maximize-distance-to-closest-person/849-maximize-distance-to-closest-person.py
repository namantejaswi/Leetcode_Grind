class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        
        first=None
        last=None
        
        for i in range(len(seats)):
            
            if seats[i]==1:
                
                if first==None:
                    first=i
                    
                last=i
                       
        #print(first,last)
                
        
        l,r=first,first
        mx=0
        
        #print(first,last)
        for i in range(first+1,last):
            
            #print(l,r)
            
            if seats[i]==0:
                r+=1
                mx=max(mx,r-l)
                
            elif seats[i]==1:
                l=i
                r=i
                
        #print (mx,first,last)
        #atleast 1 seat is empty we consider 1, taken care by first and #last as we are told atleast one seat is empty and atleast one is filled
        
       
        return max(((mx+1)/2),first,len(seats)-last-1)
                
                
        
                
                