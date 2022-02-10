class Solution:
    def findBuildings(self, nums: List[int]) -> List[int]:
        
        res=[]
        r=len(nums)-1
        
        max_left=0
        
        for i in range(len(nums)-1,-1,-1):
            
            if nums[i]>max_left:
                res.append(i)
                
            max_left=max(max_left,nums[i])
            
            
        #print(res)
        
        return res[::-1]