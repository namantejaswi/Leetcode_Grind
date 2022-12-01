class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        v1=0
        v2=0
        
        vow={'a','e','i','o','u','A','E','I','O','U'}
        
        for i in range((len(s)//2) ):
            if s[i] in vow:
                v1+=1
                
        for j in range((len(s)//2),len(s)):
            if s[j] in vow:
                v2+=1
        
        return v1==v2