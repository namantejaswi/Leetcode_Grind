class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #We first check if all the rows and columns are unique
        #Then we check if the smaller 3x3 box is unique or not
        
        def single_valid(val):
            
            res=[i for i in val if i!="."]
            
            return len(res)==len(set(res))#if we  dont get any number more than once
            
    
        def is_row_valid(board):            
            for row in board:   #Iterate over the different rows

                if single_valid(row)==False:#If one of rows is not consistent
                    return False
                
            return True
        
        
        def is_colum_valid(board):
            
            #Now we only need to check the cloumns here so we use zip with * to extract or upack to have only the columns  
            
            colum_form=zip(*board)
            
            for col in colum_form:
                
                if single_valid(col)==False:
                    return False
                
            return True
        
        
        
        def square_check(board):
            
            
            for i in (0,3,6):
                for j in (0,3,6):
                    
                    square =[board[m][n] for m in range(i,i+3)for n in range(j,j+3)]
                    
                    
                    if single_valid(square)==False:
                        return False
                    
            return True
                
        
        #print(is_row_valid(board))
        #print(is_colum_valid(board))
        
        return is_row_valid(board) and is_colum_valid(board) and square_check(board) 
        
                    
        
        
        
                