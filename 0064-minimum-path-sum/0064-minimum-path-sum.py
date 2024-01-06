class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        l = len(grid)
        w = len(grid[0])
        
        
        dp = [[float("inf") for i in range(w) ] for j in range(l)]
        
        
        #now because we dont have any negative number cell[i][j] will have min cell[i-1][j] cell[i][j-1] it wont be so if we have -ve numbers 
        
        for i in range(l):
            for j in range(w):
                

                if i==0 and j==0:   
                    print(grid[0][0])
                    dp[i][j]=grid[0][0]

                elif j==0 and i!=0:    dp[i][j]= dp[i-1][j]+grid[i][j]
                    
                elif i==0 and j!=0: dp[i][j] = dp[i][j-1]+grid[i][j]
                    
                else:   
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1])
                     
                
        return dp[-1][-1]
                    
                    
                
                    
                    
                    
                