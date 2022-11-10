class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
                
        def dfs(i,j):
            
            if i<0 or j<0 or i>=l or j>=w:
                
                return
            
            if grid[i][j]=="O":
                grid[i][j]="V"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        
        l=len(grid)
        w=len(grid[0])
        
        for i in range(l):
            for j in range(w):
                
                if ((i==l-1) or (j==w-1) or i==0 or j==0) and grid[i][j]=="O":
                    
                    dfs(i,j)
                    
                    
        for i in range(l):
            for j in range(w):
                
                if grid[i][j]=="V": 
                    grid[i][j]="O"
                    
                elif grid[i][j]=="O": grid[i][j]="X"
                    
                    
        
                    

                
                
            
                
    
            
                
                