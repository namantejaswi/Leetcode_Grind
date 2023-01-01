class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        
        #put all piles in a max heap
        #perform k operations and then return the sum
        
        
        heap_arr=[-1 * i for i in piles]
        
        
        heapq.heapify(heap_arr)
        
        for i in range(k):
            
            elem=heapq.heappop(heap_arr)
            
            val = math.floor((-1*elem)/2)
            
            heapq.heappush(heap_arr,elem+val)
            
        return -1*(sum(heap_arr))