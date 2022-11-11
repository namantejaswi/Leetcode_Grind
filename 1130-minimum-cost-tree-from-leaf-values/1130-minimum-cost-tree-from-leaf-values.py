class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        
        res=0
        
        while len(arr)>1:
            
            min_at=arr.index(min(arr))
            
            #if min is not at the start or the end of the array
            if min_at>0 and min_at<len(arr)-1:
                
                #add the product of min val and min of(l,r of min_val)
                res+=arr[min_at]*(min(arr[min_at-1],arr[min_at+1]))
                
                
            else:
                if min_at==0:   #if min at zero multiply with right
                    res+=arr[min_at]*arr[1]
                    
                    #if min at end multiply with left
                else:   res+=arr[min_at-1]*arr[min_at]
                    
            arr.pop(min_at)
            
        return res
  
