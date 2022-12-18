class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        
        char_order=[ch for index,ch in enumerate(order)]
            
            
        freq=dict(Counter(s))
        
        
        res=""
        for c in char_order:
            
            if c in freq:
                res+= c*freq[c]
                del freq[c]
                
        for rem in freq:
            res+=rem*freq[rem]
            
        return res
                
        
        
            
        