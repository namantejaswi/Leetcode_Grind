class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        count = Counter(nums)
        
        heap=[[-freq,i] for i,freq in count.items()]
        heapq.heapify(heap)
        
        res=[]
        
        for i in range(k):
            
            item = heapq.heappop(heap)
            res.append(item[1])
            
        return res