class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        from collections import deque
        #Que to store the rootten position at which we apply bfs
        
        Q_R=deque([])
        
        r=len(grid)
        c=len(grid[0])
        
        count=0
        
        for i in range(r):
            for j in range(c):
                
                if grid[i][j]==2:
                    Q_R.append((i,j))
                    
                elif grid[i][j]==1:
                    count+=1
                            
        if count==0:    return 0    #if we dont uave any fresh orange
        time=0
        
        #print(Q_R)
        while Q_R:
            
            if count==0:
                return time
            for z in range(len(Q_R)):
                x,y = Q_R.popleft()
                for m, n in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                    if 0<=m<r and 0<=n<c and grid[m][n] == 1:
                        grid[m][n] = 2
                        count -= 1
                        Q_R.append((m,n))
                        
            time += 1
            
            
        return -1