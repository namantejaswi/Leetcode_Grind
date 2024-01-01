class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        
        
        dp = [[ -1 for i in range(len(s2))]for j in range(len(s1))]

        l1=len(s1)
        l2=len(s2)
        def lcs(s1,s2,l1,l2):

            if l1>=len(s1) or l2>=len(s2):  return 0

            if dp[l1][l2]!=-1: return dp[l1][l2]

            if s1[l1]==s2[l2]:

                dp[l1][l2]= 1+lcs(s1,s2,l1+1,l2+1)
                return dp[l1][l2]

            else:
                dp[l1][l2] = max( lcs(s1,s2,l1+1,l2),lcs(s1,s2,l1,l2+1))

                return dp[l1][l2]

        return lcs(s1,s2,0,0)