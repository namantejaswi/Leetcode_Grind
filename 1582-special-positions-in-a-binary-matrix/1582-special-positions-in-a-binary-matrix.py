class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        
        cnt =0
        
        l=len(mat)
        w=len(mat[0])
        
        row_count=[0]*l
        col_count=[0]*w
        
        for i in range(l):
            for j in range(w):
                
                if mat[i][j]==1:
                    row_count[i]+=1
                    col_count[j]+=1
                    
        #print(row_count,col_count)
                    
        for i in range(l):
            for j in range(w):
                if mat[i][j]==1:
                    
                    if row_count[i]==1 and col_count[j]==1:
                        cnt+=1
                        
        return cnt
                