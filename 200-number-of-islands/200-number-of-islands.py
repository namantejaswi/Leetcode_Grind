class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
       
    
        count=0
        
        l=len(grid)
        w=len(grid[0])
             
        def dfs(grid,x,y):
        
            if  x<0 or y<0 or x>=l or y>=w or grid[x][y]!="1":
                return 
        
            else:
                grid[x][y]="0"
                dfs(grid,x+1,y)
                dfs(grid,x-1,y)
                dfs(grid,x,y-1)
                dfs(grid,x,y+1)
        
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]=="1":

                    count+=1
                    dfs(grid,i,j)
                    
        return count
    
    
    
    
    
    
    
   
            
            
                    
                    
                    