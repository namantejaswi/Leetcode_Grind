class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #To rotate by 90 degree clockwise is same as transposing and reversing rows
        
        
        c=len(matrix[0])-1
        print(c)
        
        
        #Transpose
        
        l=len(matrix)                       #------
                                            # -----
        for i in range(len(matrix)):        #  ----
            for j in range(i+1,l):          #   ---
                                            #    --
                                            #     -  
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    
        #print(matrix)
        
        
        
        
        #Reverse
        for i in range(len (matrix)):
            
            for j in range(0,(c//2)+1):
                
                #print("i",i,"j",j,"c-j",c-j)

                matrix[i][j],matrix[i][c-j]=matrix[i][c-j],matrix[i][j]
        
      
