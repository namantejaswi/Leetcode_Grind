class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        dp=[0]*(len(s)+1)
        
        dp[0]=True
        for start_index in range(len(s)):
            
            #can we have something to divide on rhs in word
            if dp[start_index]:
                for j in range(start_index, len(s)):
                    if s[start_index: j+1] in wordDict:
                        dp[j+1] = True
                        
        return dp[-1]