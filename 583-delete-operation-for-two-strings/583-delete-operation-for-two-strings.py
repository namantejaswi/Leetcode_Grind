class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        
        #The same as longest common substring
        #minimum number of deletions = length of both string - lcs
        
        dp=[[-1 for i in range(len(word2))] for j in range(len(word1))]
        #print(dp)
        
        def lcs(word1,word2,l1,l2):
            
            
            if l1==0 or l2==0:
                return 0
            
            if dp[l1-1][l2-1]!=-1:  return dp[l1-1][l2-1]
            
            elif word1[l1-1]==word2[l2-1]:
                
                dp[l1-1][l2-1]= 1+lcs(word1,word2,l1-1,l2-1)
                return dp[l1-1][l2-1]
                
            else:
               
                dp[l1-1][l2-1]= max(lcs(word1,word2,l1-1,l2),lcs(word1,word2,l1,l2-1))
                return dp[l1-1][l2-1]

        return len(word1)+len(word2) - 2*lcs(word1,word2,len(word1),len(word2))      