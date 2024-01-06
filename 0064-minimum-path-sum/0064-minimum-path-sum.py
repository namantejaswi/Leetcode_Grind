class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        l = len(grid)
        w = len(grid[0])
        
        
        dp = [[float("inf") for i in range(w) ] for j in range(l)]
        
        
        #now because we dont have any negative number cell[i][j] will have min cell[i-1][j] cell[i][j-1] it wont be so if we have -ve numbers 
        
        for i in range(l):
            for j in range(w):
                

                if i==0 and j==0:   pass

                elif j==0 and i!=0:    grid[i][j]+= grid[i-1][j]
                    
                elif i==0 and j!=0: grid[i][j] +=grid[i][j-1]
                
                else:   
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
                     
                
        return grid[-1][-1]
                    
                    
                
                    
                    
                    
                