class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        
        #8 Direction Bfs to find the shortest path
        
        if grid[0][0]==1:  return -1    #cant start
        
        q=deque()
        visited=set()
        l=len(grid)
        
        steps=1
        q.append((0,0,1))   #x,y,length of path
        
        visited.add((0,0))
        
        while q:
            
    
            x,y,steps=q.popleft()
        
            
            if x==l-1 and y==l-1: 
                return steps
            
            if grid[x][y]==1:   continue
                
                

            for i,j in((x+1,y),(x-1,y),(x+1,y+1),(x-1,y+1),(x-1,y-1),(x,y-1),(x,y+1),(x+1,y-1)):

                if i>=0 and j>=0 and i<l and j<l and (i,j) not in visited and grid[i][j]==0:


                        q.append((i,j,steps+1))
                        visited.add((i,j))

            steps+=1
            
        return -1
            