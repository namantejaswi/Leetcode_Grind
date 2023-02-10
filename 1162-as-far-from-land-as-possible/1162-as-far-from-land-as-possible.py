class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        
        #we perform a bfs from all the initial inslands to see how far can we reach
        # before we get another island
        
        mx=0
        q =deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
    
                if grid[i][j]:  q.append((i,j))
                           
        
        while q:
                           
                row,col = q.popleft()
                           
                for r,c in ((1,0),(0,1),(-1,0),(0,-1)):
                           
                           
                    r_ , c_ = row+r, col+c 
                           
                    if r_>=0 and r_<len(grid) and c_>=0 and c_<len(grid[0]) and not grid[r_][c_]:
                           
                        q.append((r_,c_))
                        grid[r_][c_]=1+grid[row][col]
                        mx=max(mx,grid[r_][c_])

                           
                           
        return mx-1
                           
                           