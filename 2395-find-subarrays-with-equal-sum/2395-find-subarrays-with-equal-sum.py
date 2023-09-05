class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        
        st = set()
        
        for i in range(len(nums)-1):
            
            s = nums[i]+nums[i+1]
            if nums[i]+nums[i+1] in st: return True
            
            else:   st.add(nums[i]+nums[i+1])   
                
        return False