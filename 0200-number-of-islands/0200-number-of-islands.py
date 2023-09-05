class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        visited = set()
    
        
        r=len(grid)
        c=len(grid[0])
        
        count = 0
        
        def dfs(x,y):
            
            if x>=r or y>=c or x<0 or y<0:  return 
            
            elif (x,y) in visited  or grid[x][y]=="0":    return 
            
            
            elif grid[x][y]=="1":
                
        
                visited.add((x,y))
                grid[x][y]="0"
                
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)
                
            
            
        for i in range(r):
            for j in range(c):
                
                if grid[i][j]=="1":   
                    count+=1
                    dfs(i,j)
                
        return count