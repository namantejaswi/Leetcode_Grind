class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        
        #if a cup gets x amount of champagne then its lower left and lower right cup
        #will get x-1 /2 amount of champagne each
        
        #if the index of glass is say r,c then x-1 /2 will flow towards glass at r+1,c and r+1, c+1
        
        #we cannot actually intiallize a traingle so we use grid with unused cells
        
        
        dp=[[0]*l for l in range(1,102)]
        dp[0][0]=poured
        
        for r in range(query_row+1):
            for c in range(r+1):
                volume=(dp[r][c]-1.0)/2
                if volume>0:
                    dp[r+1][c]+=volume
                    dp[r+1][c+1]+=volume
            
            
        return min(1,dp[query_row][query_glass])