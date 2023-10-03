class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        cnt = 0
        
        freq = dict()
        
        
        for i in range(len(nums)):
            
            if nums[i] in freq:
                
                cnt+=freq[nums[i]]
                freq[nums[i]]+=1
                
            else:   freq[nums[i]]=1
                
        return cnt