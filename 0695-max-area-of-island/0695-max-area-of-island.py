class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
    
        mx = 0 
        visited = set()
        
        def dfs(x,y):
            
            if x<0 or y<0 or x>=len(grid) or y >= len(grid[0]) or (x,y) in visited or grid[x][y]==0:         
                return 0
            
        
            else:   
                visited.add((x,y))
                return 1+dfs(x+1,y)+dfs(x-1,y)+dfs(x,y-1)+dfs(x,y+1)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                area = dfs(i,j)
                mx = max(mx,area)
                
                
        return mx
            
            