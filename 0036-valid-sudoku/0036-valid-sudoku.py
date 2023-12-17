class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        row = [set() for i in range(9)]
        col = [set() for j in range(9)]
        grid = [ set() for i in range(9)]
        
        #we have each position for a particular indexed row,col and grid
        
        
        for i in range(9):
            for j in range(9):
                
                cur_val = board[i][j]
                    
                if cur_val==".":   continue


                if cur_val in row[i]:  return False
                row[i].add(cur_val)

                if cur_val in col[j]:   return False 

                col[j].add(cur_val)

                grid_number = (i//3)*3 + j//3

                if cur_val in grid[grid_number]:    return False
                grid[grid_number].add(cur_val)

                    
                    
        return True