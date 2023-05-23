class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k=k
        self.heap = nums
        heapq.heapify(self.heap)
        
        #We need only k elements in heap, heappop heapifies after poping
        
        while len(self.heap)>k: heapq.heappop(self.heap)
            
        
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        
        #if on adding the curr element the heap exceedes k we pop
        
        if len(self.heap)>self.k:   heapq.heappop(self.heap)
        
        return self.heap[0]     #min heap of k length kth largest elment will be smallest


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)