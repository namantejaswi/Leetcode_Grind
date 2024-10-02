class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        
        rank = {}
        
        
        for n in sorted(arr):
            
            if n in rank:   continue
                
            else:   rank[n] = len(rank)+1
                
                
        res=[]
        
        for i in arr:
            res.append(rank[i])
            
        return res