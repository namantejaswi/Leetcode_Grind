class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        
        
        n=len(mat)
        
        dp=[[float('inf') for i in range(n)] for j in range(n)]
        
        def calc(row,col):
            
            if row==n:  return 0    #We have already reached the last row 
            
            
            elif col==n or col<0:   return float('inf')     #we consider the distance infinity as it is not possible to be here
            
            elif dp[row][col]!=float('inf'):  return dp[row][col]
            
            
            #we select the current cell and next cell is choosen as the minimum path starting with the 3 chocies
            
            choose_down=calc(row+1,col)
            choose_left=calc(row+1,col-1)
            choose_right=calc(row+1,col+1)
            
            dp[row][col]=mat[row][col]+ min(choose_down,choose_left,choose_right)
            return dp[row][col]
        
        
        #we consider all starting points in the first row and subsequently l,r down are considered in the recursive call calc
        min_path=float('inf')
        for c in range(n):
        
            min_path=min(calc(0,c),min_path)    
        return min_path