class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        l=len(matrix)
        w=len(matrix[0])
        
        left=0
        top=0
        right=w-1
        bottom=l-1
        
        res=[]
        
        while left<=right and top<=bottom:
            
            for col in range(left,right+1):
                
                res.append(matrix[top][col])
                
            top+=1
            
            
            for row in range(top,bottom+1):
                
                res.append(matrix[row][right])
                
            right-=1
            
            
            for col in range(right,left-1,-1):
                
                res.append(matrix[bottom][col])
                
            bottom-=1
            
            for row in range(bottom,top-1,-1):
                
                res.append(matrix[row][left])
                
            left+=1
            
        
        return res[:l*w]
            
            