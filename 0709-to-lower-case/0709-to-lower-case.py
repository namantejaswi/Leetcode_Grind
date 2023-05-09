class Solution:
    def toLowerCase(self, s: str) -> str:
        
        
        def is_upper(x):
            if (x>="A" and x<="Z"): return True
        
        to_lower = lambda x:  chr(ord(x)+32)
        
        res=""
        for ch in s:
            
            if is_upper(ch):
                res+=to_lower(ch)
                
            else:   res+=ch
                
        return res