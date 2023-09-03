class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        
        if  grid[0][0]==1: return 0 
    
        r=len(grid)
        c=len(grid[0])
    
        dp=[[0 for i in range(c)] for i in range(r)]
        dp[0][0]=1
        
        #dp [i][j] represents the number of possible paths to reach the current index
        
        
        
        for i in range(r):
            
            if grid[i][0]==1: 
                dp[i][0]=0
                break
                
            else:    dp[i][0]=1

                            
                
        for j in range(c):
        
            if grid[0][j]==1:
                dp[0][j]=0
                break
                
            else:    dp[0][j]=1
            

        for i in range(1,r):
            for j in range(1,c):                
            
                if grid[i][j]==1:   dp[i][j]=0  #no way to reach here
            
                else:    dp[i][j]=dp[i-1][j]+dp[i][j-1] 
                   
        return dp[-1][-1]
                
    
