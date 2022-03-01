class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones=[-1* i for i in stones]
        
        
        heapq.heapify(stones)
        
        while(len(stones)>1):
            
            st1=heapq.heappop(stones)
            
            st2=heapq.heappop(stones)
        

            if st1<st2:
                st1=st1-st2
                heapq.heappush(stones,st1)
                
        if len(stones)==0: return 0       
        return -1*stones[0]