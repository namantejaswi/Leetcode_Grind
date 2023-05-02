class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        
        d1 = dict(Counter(s))
        d2 = dict(Counter(t))
        
        #so we find the common letters in s and t and count their frequency and then subtract from the total length of t
        
        
        common=0
        
        for k,v in d2.items():
            
            if k in d1:
                common+=min(d1[k],d2[k])
                
        #print(common)
        
        return len(t)-common
            