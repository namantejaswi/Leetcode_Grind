class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                
                #if we are not at the starting grid
                if i>0 and j>0:
                    
                    #modify grid to represent the minimum cost to reach that point
                    
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
                    
                    
                elif i==0 and j>0:
                    #in the oth row we can reach using only right moves
                    
                    grid[i][j]+=grid[i][j-1]
                    
                elif i>0 and j==0:
                # in the same col we can only rech by going down
                
                    grid[i][j]+=grid[i-1][j]
                    
                    
        return grid[-1][-1]