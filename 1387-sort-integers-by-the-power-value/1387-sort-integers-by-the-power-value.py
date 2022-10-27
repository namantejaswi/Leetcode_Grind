class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        
        dp={1:1}
        
        
        def calc(n):
            
            if n in dp: return dp[n]
            
            else:
                
                if n%2==0:
                    
                    dp[n]=1+calc(n//2)
                    return dp[n]
                    
                else:
                    
                    dp[n]=1+ calc(3*n+1)
                    
                    return dp[n]
                
                
        ans= sorted((calc(i),i) for i in range(lo,hi+1))
        return ans[k-1][1]    
                
                
                    