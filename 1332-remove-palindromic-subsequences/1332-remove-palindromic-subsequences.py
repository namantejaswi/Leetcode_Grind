class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        
        
        #we remove 2 subsequences at most since the list only has a and b
        #so if it is a palindrome we remove one subsequence else we remove 2
        
        
        s=list(s)
        rptr=len(s)-1
        lptr=0
        
        while(rptr>lptr):
            
            if s[lptr]!=s[rptr]:    
                return 2
            lptr+=1
            rptr-=1
            
        return 1
        
        