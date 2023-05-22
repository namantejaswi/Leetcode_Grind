class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        
        if numRows ==1 or numRows>=len(s):  return s
        
        grid = [""]*numRows
        index = 0
        step = 1
        
        for i in s:
            
            grid[index]+=i
            
            if index == 0:   step=1
                
            elif index ==  numRows-1:       step=-1
                
            index+=step
            
        return "".join(grid)
            