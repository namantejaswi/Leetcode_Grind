class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        l2=math.ceil(len(arr)//2)
        freq=dict(Counter(arr))
        
        h=[]
        for i in freq.values():
            h.append(-i)
        
        heapq.heapify(h)
        num=0
        cnt=0
        while num<l2 and h:
            
            num+=-heapq.heappop(h)
            cnt+=1
            
        return cnt
        
        