class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        #longest palindromic subsequence is the same as finding the longest common subsequence between the given string and the reversed string
        
        
        s2=s[::-1]
        
        l1,l2=len(s)-1,len(s2)-1
        
        dp = [[-1 for i in range(len(s))] for j in range(len(s))]
        
        
        def lcs(s,s2,l1,l2):
            
            if l1==-1 or l2==-1:    return 0
                
            elif dp[l1][l2]!=-1:    return dp[l1][l2]
            
            elif s[l1]==s2[l2]:  
                
                dp[l1][l2]=1+lcs(s,s2,l1-1,l2-1)
                return dp[l1][l2]
            
            else:   
                dp[l1][l2]= max(lcs(s,s2,l1,l2-1),lcs(s,s2,l1-1,l2))
                return dp[l1][l2]
        
        
        return lcs(s,s2,l1,l2)