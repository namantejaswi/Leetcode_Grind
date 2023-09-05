class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        heap = []   #min heap where we store our k elements with the smallest one being at the root
        
        
        for i in nums:
            
            if len(heap) <k:
                
                heapq.heappush(heap,i)
                
            elif i >heap[0]:
                
                heapq.heappushpop(heap,i)
         
        return heap[0]
                
            