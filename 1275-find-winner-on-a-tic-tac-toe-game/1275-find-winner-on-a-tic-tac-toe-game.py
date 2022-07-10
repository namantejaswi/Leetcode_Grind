class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        #player wins if we have any diagonal row or col
        #+ve diag c+r
        #-ve diag c-r
        
        grid=[[0 for i in range(3) ]for j in range(3)]
        
        turn=0
        for m in moves:
            
            if turn%2==0:
                grid[m[0]][m[1]]="A"
            
            else:   grid[m[0]][m[1]]="B"
        
            turn+=1
                    
        #print(grid)
        
        #check all row, col diagonal can use bitwise as well to speed up
        
        r1=grid[0]
        if r1[0]==r1[1] and r1[1]==r1[2] and r1[0]!=0:
            return r1[0]
        r2=grid[1]
        if r2[0]==r2[1] and r2[1]==r2[2] and r2[0]!=0:
                return r2[0]
        r3=grid[2]
        if r3[0]==r3[1] and r3[1]==r3[2] and r3[0]!=0:
                return r3[0]
            
        #i+j=coonstant +ve diag j-i=const negative diag
        #but for 3 can calc by hand
        
        diag_1=[grid[0][0],grid[1][1],grid[2][2]]
        if diag_1[0]==diag_1[1] and diag_1[1]==diag_1[2] and diag_1[0]!=0:
            return diag_1[0]
        
        diag_2=[grid[0][2],grid[1][1],grid[2][0]]
        if diag_2[0]==diag_2[1] and diag_2[1]==diag_2[2] and diag_2[0]!=0:
            return diag_2[0]
        
        
        c1=[grid[0][0],grid[1][0],grid[2][0]]
        if c1[0]==c1[1] and c1[1]==c1[2] and c1[0]!=0:
                return c1[0]
            
        c2=[grid[0][1],grid[1][1],grid[2][1]]
        if c2[0]==c2[1] and c2[1]==c2[2] and c2[0]!=0:
                return c2[0]
            
        c3=[grid[0][2],grid[1][2],grid[2][2]]
        if c3[0]==c3[1] and c3[1]==c3[2] and c3[0]!=0:
                return c3[0]
            
        elif len(moves)<9:  return "Pending"
        
        else:   return "Draw"
      
        
        
        