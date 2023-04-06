class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        l = len(grid)
        w = len(grid[0])
        
        
        def dfs ( r, c):
            
        
            if  r<0 or c<0 or r==l or c==w:  return False
            
            #we found the boundary in one direction
            elif grid[r][c]==1 or (r,c) in visited:   return True 
            
            
            visited.add((r,c))
            
            #logiacal and to make sure all 4 dfs call have an boundary 
            
            return dfs(r+1,c) & dfs(r-1,c) & dfs(r,c+1) & dfs(r,c-1)
            

        cnt=0
        for r in range(l):
            for c in range(w):
                if grid[r][c]==0 and (r,c) not in visited:  cnt+=dfs(r,c)        
        return cnt