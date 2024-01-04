class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        ans=0
        dp = {}
        
        def dfs(x,y,moves):
            
            if (x,y,moves) in dp: return dp[(x,y,moves)]
            
            if (x,y,moves) in dp: return dp[(x,y,moves)]
            if moves>maxMove: return 0
            
            if x<0 or y<0 or x>=m or y>=n:
                return 1
            
            else:
                dp[(x,y,moves)]= dfs(x+1,y,moves+1)+dfs(x-1,y,moves+1)+dfs(x,y-1,moves+1) +dfs(x,y+1,moves+1)
                return dp[(x,y,moves)]
                
            
        
        return dfs(startRow,startColumn,0)%((10**9)+7)
                
                
                
            