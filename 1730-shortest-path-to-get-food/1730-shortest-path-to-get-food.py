class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        #follow bfs to get the shortest path
        
        #first find the start location
        
        start=None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]=="*":
                    start=(i,j,0)
                    break
                    
        
        q=collections.deque()
        
        q.append(start)
        
        
        while q:
            x,y,count=q.popleft()
            
            if grid[x][y]=="X":   continue
            elif grid[x][y]=="#":     return count
            
            #Regardless of what happens mark current cell as visited
            
            grid[x][y]="X"
            
            directions=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            
            for i, j in directions:
            
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 'X':
                    q.append((i, j, count + 1))
        
            
        return -1
            