class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        res = set()
        
        nums.sort()

        def two_sum(idx):
        
            
            lptr = idx + 1
            rptr = len(nums)-1

            while lptr<rptr:

                val = nums[lptr]+nums[rptr]+nums[idx]
                if val==0:  
                    res.add((nums[idx],nums[lptr],nums[rptr]))
                    lptr+=1
                    rptr-=1
                    while lptr<rptr and nums[lptr]==nums[lptr-1]:   lptr+=1
                    
                    
                elif val<0: lptr+=1

                elif val>0: rptr-=1
                

        
        for i in range(len(nums)):
            
        #if curr is +ve the remainins numbeers to right are also+ve so cant sum to 0
            
            if nums[i]>0:   break 
                
            else:  two_sum(i)
                
            
        ans = []
        for tupple in res:
            ans.append(list(tupple))
            
        return ans
                
                

                
                
                
        
            