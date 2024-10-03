class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
   
        target = sum(nums) % p
        if target == 0:
            return 0

        prefix_sum = {0: -1}
        current_sum = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            complement = (current_sum - target) % p
            
            if complement in prefix_sum:
                min_length = min(min_length, i - prefix_sum[complement])
            
            prefix_sum[current_sum] = i

        return min_length if min_length < len(nums) else -1