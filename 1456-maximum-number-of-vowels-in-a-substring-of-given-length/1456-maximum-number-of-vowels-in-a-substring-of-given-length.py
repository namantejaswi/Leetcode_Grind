class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        
        mx=0
        l=0
        r=k-1
        vow={'a','e','i','o','u'}
        cnt=0
        mx=0
    
    
        for index,val in enumerate(s):
            
            if index>=k:
                
                if s[index-k] in vow:
                    cnt-=1
                    
            if s[index] in vow:
                cnt+=1
                
        
            mx=max(mx,cnt)
            
            
        return mx