class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        
        res = []
        
        mx= [-1 for i in range(len(matrix[0]))] 
        mi = []
        
        
        for i in matrix:
                mi.append(min(i))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                mx[j]=max(mx[j],matrix[i][j])
                
        
        mx = set(mx)
        
        for i in mi:    
            if i in mx:
                res.append(i)
                
        return res
                
        
        