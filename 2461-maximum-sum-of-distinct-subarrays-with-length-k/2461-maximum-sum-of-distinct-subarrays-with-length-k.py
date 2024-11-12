class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        
        l = 0
        st = set()
        
        curr_sum = 0
        mx = 0
        
        
        for r in range(len(nums)):
            
            
            #remove duplicates if nums[r] already in set by increasing l
            
            
            while nums[r] in st:
                st.remove(nums[l])
                curr_sum -= nums[l]
                l+=1
                
            st.add(nums[r])
            curr_sum+=nums[r]
            
            if r-l+1>k:     #2 elements make window of 2 but their diff is 1
                
                curr_sum -=nums[l]
                st.remove(nums[l])
                l+=1
                
                
            #now if our window is of k lenth compare mx
            
            
            if r-l+1==k:
                mx = max(mx, curr_sum)
                
                
        return mx
                
                
                