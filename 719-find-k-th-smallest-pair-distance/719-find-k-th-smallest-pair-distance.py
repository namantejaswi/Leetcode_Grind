class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        #dis=[]
        
        #for i in range(len(nums)):
         #   for j in range(i+1,len(nums)):
          #      dis.append(abs(nums[i]-nums[j]))
                
        #heapq.heapify(dis)  #we build a min heap
        
        #pop k-1 elements 0,1,2,..k-2 elements are removed total k-1 elements removed
        #kth element then will be the root
        
        #for c in range(k-1):
         #   heapq.heappop(dis)  
            
        #return dis[0]
        
        
        
        def smaller_pairs(mid):
            lptr=0
            rptr=0
            cnt=0
            for rptr in range(len(nums)):
                while nums[rptr] - nums[lptr] > mid:
                    lptr += 1
                cnt += rptr - lptr
            return cnt

        nums.sort()
        lo=0
        hi= nums[-1] - nums[0]
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if smaller_pairs(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
            
            
            
            

        