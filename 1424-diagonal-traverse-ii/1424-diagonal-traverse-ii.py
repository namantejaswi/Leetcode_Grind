class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        col=0
        
        for row in nums:
            col = max(col,len(row))
            
        diag = col + len(nums) -1
        
        
        
        res = [[] for k in range(diag)]
        
        
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                
                res[i+j].append(nums[i][j])
                
                
        ans=[]
        
        
        idx=1
        

        
                
        for arr in res:
            #print(arr)
            for val in arr[::-1]:
                ans.append(val )
                
        return ans