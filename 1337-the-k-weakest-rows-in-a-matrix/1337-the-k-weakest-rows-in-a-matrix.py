class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        
        r = []
        
    
        for i in range(len(mat)):
           
            r.append([sum(mat[i]),i])       #sum, indices
            
        heapq.heapify(r)
        
        res=[]
        
        for i in range(k):
            
            res.append(heapq.heappop(r)[1])    #heappop heapifies after poping
            
            
        return res