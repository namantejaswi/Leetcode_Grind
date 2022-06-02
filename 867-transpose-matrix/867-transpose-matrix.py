class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        mat=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(len(matrix)):
                temp.append(0)
                
            mat.append(temp)
            
        #print(mat)
                
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                                
                mat[i][j]=matrix[j][i]
                
        return mat
            