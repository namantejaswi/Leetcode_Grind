class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        
        
        return len(nums) - max(Counter(nums).values())

        
        
        
#         nums.sort()
        
#         res=0
#         for n in nums:
#             if n>nums[res]:
#                 res+=1
                
#         return res