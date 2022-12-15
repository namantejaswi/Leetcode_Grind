class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        
        dp=[[-1 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        
        
        
        def lcs(idx1,idx2):
            
            if idx1==-1 or idx2==-1:    return 0
            
            if dp[idx1][idx2]!=-1 : return dp[idx1][idx2]
            
           
            elif text1[idx1]==text2[idx2]:
                
                dp[idx1][idx2]= 1+lcs(idx1-1,idx2-1)
                return dp[idx1][idx2]            
            else:
                
               
                dp[idx1][idx2]= (max((lcs(idx1-1,idx2)),lcs(idx1,idx2-1)))            
                return dp[idx1][idx2]
            
            
        return lcs(len(text1)-1,len(text2)-1)
        