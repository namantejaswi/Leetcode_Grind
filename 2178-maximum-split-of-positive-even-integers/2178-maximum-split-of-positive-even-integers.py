class Solution:
    def maximumEvenSplit(self, s: int) -> List[int]:
        
        
        if s%2!=0: return []
        
        
        res=[]
        n=2
        
        while s>=n:
            res.append(n)
            s-=n
            n+=2
            
        #once number is greater than sum remaining add the remaining sum to last
        #if perfectly split we will be adding zero
        
        
        res[-1]+=s
            
            
        return res
