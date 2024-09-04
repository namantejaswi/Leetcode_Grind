class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        
        
        # we populate from top left corner to bottom right corner as a dp matrix
        # if we have 1  > then we update the diagnally down index min of the 3 choices values r-1[c] [r][c-1] [r-1][c-1]
        
        
        #   \|
        #   --  choose min
    
        #if mat[i][j] ==1
        # dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
        
        #we set dp to zero and only check/update when we get some non zero number in grid
        
        #now we add a pad of 1 row and col to dp so we can init dp 0 row and col without underflow in orignal matrix
        
        
        #if we have a square full of ones to extend it we go to the next diagnoal cell and check if previous row and 
        
        dp = [[0 for j in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        
        mx=0
        
    
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                  
                if mat[i-1][j-1]=="1":
                    
                    dp[i][j] = 1+min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                    mx=max(mx,dp[i][j])     
        
        return mx*mx
                    
                    
                    