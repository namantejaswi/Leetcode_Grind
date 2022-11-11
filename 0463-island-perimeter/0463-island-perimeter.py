class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        peri=0
        
        l=len(grid)
        w=len(grid[0])
        
        for i in range(l):
            for j in range(w):
                
                if grid[i][j]==1:
                    
                    bound=4
                    
                    #if neighbour to the left x directionally perimeterr reduces by 2
                    #coz the 2 sides merge
                    #  _     _
                    # |_|---|_| insted of 4+4 2+2
                    #
                    #same thing vertically
                    #
                    if i>0 and grid[i-1][j]==1: bound-=2
                        
                    if j>0 and grid[i][j-1]==1: bound-=2
                        
                    peri+=bound    
                    
                    
        
        return peri