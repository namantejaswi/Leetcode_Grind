class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        dp = {}
        
          
            
            
        def lcs(l1,l2):
            
            
            if l1 == len(s1)  or l2 == len(s2): return 0 
            
            elif (l1,l2) in dp:    return dp[(l1,l2)]
            
            elif s1[l1]==s2[l2]:
                
                dp[(l1,l2)]= 1+lcs(l1+1,l2+1) 
                return dp[(l1,l2)]            
            
            else:   
                dp[(l1,l2)]=max(lcs(l1+1,l2),lcs(l1,l2+1))
                return dp[(l1,l2)]
        
        return lcs(0,0)
      
            
        