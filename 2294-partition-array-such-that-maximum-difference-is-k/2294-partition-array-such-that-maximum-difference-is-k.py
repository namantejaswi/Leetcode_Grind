class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        
        
        #the term subsequence has no bearing as whatever order we select from an    
        #array it will always be a subsequence
        
        
        if not nums:    return 0
        
        count=1
        prev=0
        
        nums.sort()
        
        for curr in range(len(nums)):
            
            if nums[curr]>nums[prev]+k:
                count+=1
                prev=curr
                
        return count