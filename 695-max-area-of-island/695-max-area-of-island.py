class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        r=len(grid)
        c=len(grid[0])
        
        def dfs(i,j):
            
            if i>=0 and i<r and j>=0 and j<c and grid[i][j]==1:
                
                grid[i][j]=0    #once counted mark as zero
                return 1+dfs(i+1,j) + dfs(i,j+1) + dfs(i-1,j) + dfs(i,j-1)
        
            else:   return 0

        mx=0
        a=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    a=dfs(i,j)
                    mx=max(a,mx)
                
        return mx
                
        