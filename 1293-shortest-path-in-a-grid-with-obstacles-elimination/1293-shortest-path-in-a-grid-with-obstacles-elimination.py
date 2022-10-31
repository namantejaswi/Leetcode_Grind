class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        
        l=len(grid)
        w=len(grid[0])
        
        visited=set()
        
        
        q=deque()
        
        #Store the steps, corrdinate and the number of obstacles we can eliminate
        
        q.append([0,0,0,k])     #[steps,x,y,k]
        
        
        while q:
            
            
            elem=q.popleft()
            
            x,y=elem[1],elem[2]
            n_steps=elem[0]
            rem_k= elem[3]
                        
               
            if x==l-1 and y==w-1 and rem_k>=0:    return  n_steps
            
            #if x<0 or y<0 or x>=l or y>=w:  continue
            #Better to check before adding to q
            
            if (x,y,rem_k) in visited:  continue
            if rem_k<0: continue
                
            visited.add((x,y,rem_k))
            
            if grid[x][y]==1:   rem_k-=1
            
            for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                
                
                if i>=0 and j>=0 and i<l and j<w:   q.append([n_steps+1,i,j,rem_k])
            
            
        return -1
            
            
            
                    
                    
                    
                        
                        
                        
                    
                    