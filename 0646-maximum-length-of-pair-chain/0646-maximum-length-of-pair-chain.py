class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        
        
        
        pairs.sort(key = lambda x:x[1])
        
        mx=float('-inf')
        res =0
        
        for p in pairs:
            
            if p[0]>mx:
                res+=1
                mx=p[1]
                
        return res
        
        