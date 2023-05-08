class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        
        p_diag=0
        n_diag=0
        
        
        for i in range(len(mat)):
            for j in range(len(mat)):
            
            
                if i==j:    p_diag+=mat[i][j]
                    
                elif i+j==len(mat)-1:  n_diag+=mat[i][j]
                    
        
        
        return p_diag+n_diag
                