class Solution:
    def maxProduct(self, nums: List[int]) -> int:
       
        max_prod = min_prod = res = nums[0]
         
        for i in range(1, len(nums)):
            
            temp = max_prod
            
            max_prod = max(nums[i], max_prod * nums[i], min_prod * nums[i])
            min_prod = min(nums[i], temp * nums[i], min_prod * nums[i])
            
            res = max(res, max_prod)
        
        return res