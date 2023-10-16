class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        
        arr = []
        
        
        for i in range(rowIndex+1):
        
            arr.append([1]*(i+1))
            
        
        for i in range(2,rowIndex+1):
            
            for j in range(1,len(arr[i])-1):    #leave first and last
                
                arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
                
             
        return arr[-1]
            