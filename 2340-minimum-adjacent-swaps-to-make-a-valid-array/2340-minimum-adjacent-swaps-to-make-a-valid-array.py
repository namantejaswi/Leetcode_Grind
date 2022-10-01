class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        
        mi=min(nums)
        mx=max(nums)
        mi_idx=None
        mx_idx=None
        
        
        for i in range(len(nums)):
            
            if nums[i]==mi:
                if mi_idx==None:
                    mi_idx=i
                    
            if nums[i]==mx:
                mx_idx=i
                
           
                
        if(mi_idx>mx_idx):
            
            #if min index is first than max index we move mi to left in mi_idx-1 swaps
            # and max to right in lnth -mi swaps
            
            return  mi_idx -1+len(nums) - 1 - mx_idx 
        
        else:
            #if mx if first we move mx to left in len -1 -mx idx and mi to right by mi times index
            
            return len(nums) - 1 - mx_idx + mi_idx

        
        