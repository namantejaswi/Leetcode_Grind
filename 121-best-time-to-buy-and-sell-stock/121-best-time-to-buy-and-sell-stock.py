class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        
        
        global_min=float('inf')
        max_profit=0
        
        for i in range(len(nums)):

            if nums[i]<global_min:
                global_min=nums[i]
                
            
            else:
                max_profit=max(max_profit,nums[i]-global_min)
                
        return max_profit