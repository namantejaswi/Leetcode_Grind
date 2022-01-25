class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
    
        def findrow(matrix,target):

            low=0
            high=len(matrix)-1
            
            
            while(low<=high):
                
                mid=(low+high)//2
                
                if target>=matrix[mid][0] and target <= matrix[mid][-1]:
                    
                    return mid
                
                elif target>matrix[mid][-1]:
                    low=mid+1    
                    
                elif target<matrix[mid][0]:
                    high=mid-1
                    
            return -1
        
        def findcol(matrix,target,row):
            
            
            low=0
            high=len(matrix[row])-1
            
            while(low<=high):
                mid=(low+high)//2
                 
                    
                if matrix[row][mid]==target:
                    print(row,mid)
                    return True
        
                elif matrix[row][mid]>target:
                        high=mid-1
                    
                else:
                    low=mid+1
                    
            return False        
                    

        
        row=findrow(matrix,target)
        #print(row)
        if row==-1: return False
        
        
        return findcol(matrix,target,row)
            
                    
        
                    
                    
                
                