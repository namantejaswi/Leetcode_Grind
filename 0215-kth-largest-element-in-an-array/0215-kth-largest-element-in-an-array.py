class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        heap = []   #min heap where we store our k elements with the smallest one being at the root
        
        
        for i in nums:
            
            if len(heap) <k:
                
                heapq.heappush(heap,i)
                
            elif i >heap[0]:
                
                heapq.heappushpop(heap,i)
        #The combined action runs more efficiently than heappush() followed by a separate call to heappop().
        return heap[0]
                
            