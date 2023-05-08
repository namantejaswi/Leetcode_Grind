class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        
        #we needd to calculate the number of zeros and ones in each row and col
        
        #sum of each row andd col will tell us the number of zeros and ones
        
        l= len(grid)
        w= len(grid[0])
        
        row_ones = [0]*l
        col_ones = [0]*w
        
        
        for i in range(l):
            for j in range(w):
                
                row_ones[i]+=grid[i][j]
                col_ones[j]+=grid[i][j]
                
                
        diff = [[0 for i in range(w)]for j in range(l)]
                
            
            
        for i in range(l):
            for j in range(w):
                
                
                diff[i][j]=row_ones[i]+col_ones[j]- (l-row_ones[i])-(w-col_ones[j])
                            
                
        return diff
                
                
                
                