class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        if len(nums)<=4: return 0 #change the 3 elements to 4th
        #heap time nlogk  sort nlogn,   k=4 but need auxillary space or modify input
        
        min_heap = nums
        heapq.heapify(nums)
            
        max_heap = [-1*nums[i] for i in range(len(nums))]
        heapq.heapify(max_heap)
        
        print(min_heap, max_heap)
        
        n_largest = []
        n_smallest = []
        
        for i in range(4):
            if max_heap:
                n_largest.append(heapq.heappop(max_heap)*(-1))
                            
        for i in range(4):
            
            if min_heap:
                n_smallest.append(heapq.heappop(min_heap))
                            
        print(n_largest,n_smallest)
            
        min_diff = float("inf")
        for i in range(4):#we make other 6 element same by changing first 3 to other 3
            min_diff = min(min_diff, n_largest[i]-n_smallest[3-i]) # can reverse also
            
        return min_diff