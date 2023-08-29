class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        
        
        l1 = len(w1)
        l2 = len(w2)
        
        res=""
        idx=0
        
        for i in range((min(l1,l2))):
            
           
            res+=w1[i]
            res+=w2[i]
            idx+=1


        if idx==l1:
            res+=w2[idx:]
            
            
        else:
            res+=w1[idx:]
            
        return res
            