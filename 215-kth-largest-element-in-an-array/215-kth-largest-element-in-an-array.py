class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq
        for i in range(len(nums)):  nums[i]=-1*nums[i]
            
        heapq.heapify(nums)
        
        for i in range(k-1):
            heapq.heappop(nums)
            
        return -1*nums[0]