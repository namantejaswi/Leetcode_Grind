class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        
        res=""
        max_l=0
        
        
        for i in range(len(s)):
            
            
            def helper(l,r):
                
                nonlocal max_l
                nonlocal res
                
                while (r<len(s) and l>=0 and s[l]==s[r]):
                    
                    if r-l+1>max_l:
                        res=s[l:r+1]
                        max_l=r-l+1
                        #print(res)

                    l-=1
                    r+=1   
                    
            helper(i,i) #for odd centered problem
            helper(i,i+1)   # for even symmetric palindrome
            
        return res
                    
                