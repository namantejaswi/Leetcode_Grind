class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
        arr = [ [1]* i for i in range(1,numRows+1) ]
        #print(arr)
        
        for r in range(2,numRows):
            
            for j in range(1,len(arr[r])-1):
                arr[r][j]=arr[r-1][j-1]+arr[r-1][j]
                
                
        return arr
            
            
            