class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        freq={}
        freq[0]=1
        s=0
        count=0
        
        for i in range(len(nums)):
            s+=nums[i] 
            if s-k in freq:
                count+=freq[s-k]
                
            if s not in freq:
                freq[s]=1
                
            else:   freq[s]+=1
                
                
        return count