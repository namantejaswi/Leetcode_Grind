class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:        
        
        s2=s[::-1]
        
        l1=len(s)-1     #indexes
        l2=len(s2)-1
        
        memo=[[-1 for x in range(l1+1)] for y in range(l2+1)]
        
        def lcs(s,s2,l1,l2):
            
            #Base case
            
            if l1==-1 or l2==-1:    return 0
            
            
            elif(memo[l1][l2]!=-1): 
                
                return memo[l1][l2]
            
            elif(s[l1]==s2[l2]):
                
                memo[l1][l2]=1+lcs(s,s2,l1-1,l2-1)
                return memo[l1][l2]
                
            else:
                memo[l1][l2]=max(lcs(s,s2,l1-1,l2),lcs(s,s2,l1,l2-1))
                return memo[l1][l2]
                
        return lcs(s,s2,l1,l2)
                
           