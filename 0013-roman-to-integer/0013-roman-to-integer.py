class Solution:
    def romanToInt(self, s: str) -> int:
        
        
        int_val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        res=0
        
        for i in range(len(s)-1):
            
            if int_val[s[i]]>=int_val[s[i+1]]:
                
                res+=int_val[s[i]]
                
                
            else:   res-=int_val[s[i]]
                
        res+=int_val[s[-1]]
        
        return res
        