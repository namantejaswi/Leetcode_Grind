class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        
        dp={}
        
        for w in words:
            if w not in dp:
                dp[w]=1
                
                
        for w in sorted(words, key=len):    #sort by length
            
            for i in range(len(w)):
                
                #try skipping all chars at index i iteratively
                s=w[:i]+w[i+1:]
                
                if s in dp:
                    
                    dp[w]=max(dp[w],dp[s]+1)
                    
                    
        return(max(dp.values()))