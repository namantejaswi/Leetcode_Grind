class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
    
    #subarray's sum must be equalt to target
    
        s=set()
        s.add(0)
        
        count=0
        prefix_sum=0
        
        for i in range(len(nums)):
            
            prefix_sum+=nums[i]
            if prefix_sum-target in s:
                count+=1
                #if we take an array reset the prefix sum and all the intermediate subarray sum stored in s since that can't be used as we need only non overlapping subarrays
                s=set()
                prefix_sum=0
            s.add(prefix_sum)
                
        return count
                
                
                
            
            
        