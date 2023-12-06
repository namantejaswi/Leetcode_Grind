class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        
        
        extra = dict()      # dictionary to store count of extra stone at index (i,j)
        empty = []
        
        
        for i in range(3):
            for j in range(3):
                
                if grid[i][j] == 0: empty.append([i,j])
                    
                elif grid[i][j] >= 1: extra[(i,j)] =grid[i][j]
                
        #print(extra,empty)  
        
        def dfs(idx):
            
            if idx == len(empty): return 0 #no cost
            
            mi = float('inf')
            
            x,y = empty[idx]
    
            
            for (m,n) in extra:
                
                if extra[(m,n)]==1: continue
                    
                else:
                    #brute force ideal locations to distribute stones
                    
                    extra[(m,n)]-=1
                    
                    mi = min(mi, dfs(idx+1) +abs(m-x)+abs(n-y))
                    
                    extra[(m,n)] +=1
                    
            return mi
        
        return dfs(0)
                    
                    
            
                    
        