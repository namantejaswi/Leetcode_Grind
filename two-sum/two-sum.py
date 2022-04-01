class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        
        dic={}
        
        for i in range(len(nums)):
            
            dic[nums[i]]=i
            
        for j in range(len(nums)):
        
            complement=target-nums[j]
            
            if complement in dic and dic[complement]!=j:
                
                
                #dic[complement]!=j ensures that the same element at same index
                #is not used to add up to the, eg [2,3,5,6,7,1] t=4 2,2 wont do
                
                return (j,dic[complement])
                
            
            
          