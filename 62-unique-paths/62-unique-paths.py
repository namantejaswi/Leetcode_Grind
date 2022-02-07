class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
    
    
        dp=[[0 for i in range(n)] for j in range(m)]
        #print(dp)
        
       
        for col in range(0,n):
            dp[0][col]=1
       
        
        for row in range(0,m):
            dp[row][0]=1
            
        #print(dp)
        
        
        #ycordinat m is number of rows
        #xcordinate n is number of columns
        
        
        for r in range(1,m):
            for c in range(1,n):
                
                dp[r][c]=dp[r-1][c]+dp[r][c-1]
                
        return dp[-1][-1]
        
        
        
        
        