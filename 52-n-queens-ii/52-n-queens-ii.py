class Solution:
    def totalNQueens(self, n: int) -> int:
        
        
        
        cols=set()
        p_diag=set()     #c+r
        n_diag=set()     #c-r
        
        
        
        cnt=0
        
        def back_track(r):
            nonlocal cnt   # if we diefint cnt - o here on every call it will set to 0
            
            if r==n:
                cnt+=1
                
                
            for c in range(n):
                
                if c in cols or c+r in p_diag or c-r in n_diag:
                    continue
                    
                else:
                    cols.add(c)
                    p_diag.add(c+r)
                    n_diag.add(c-r)
                    
                    
                    back_track(r+1)
                    
                    cols.remove(c)
                    p_diag.remove(c+r)
                    n_diag.remove(c-r)
                    
                    
        back_track(0)
        return cnt
        
            
            
            
        