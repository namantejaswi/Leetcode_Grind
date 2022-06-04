class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        
        cols=set()
        p_diag=set()
        n_diag=set()
        
        res=[]
        board=[["."]*n for i in range(n)]
        
        #print(board)
        
        
        def valid_sol(r):
            
            #Base case
            
            if r==n:    
                #print(board,"d")
                valid=["".join(row) for row in board]
                res.append(valid)
                
                
            for c in range(n):  #indexing of board from zero n no. of rxc
                
                
                if c in cols or c+r in p_diag or c-r in n_diag:
                    
                    continue

                board[r][c]="Q"
                cols.add(c)
                p_diag.add(c+r)
                n_diag.add(c-r)

                valid_sol(r+1)  #Recurssive call for next row

                cols.remove(c)
                p_diag.remove(c+r)
                n_diag.remove(c-r)

                board[r][c]="."
                    
        valid_sol(0)
        return res
                    
                    
                    
            
            
            