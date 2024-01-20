class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        res = []
        triplet = set()
        nums.sort()
        
        #we find 2 numbers such that nums[idx]+nums[n1]+nums[n2]=target
        
        def two_sum(idx):
            
            lptr=idx+1
            rptr=len(nums)-1
            
            while lptr<rptr:
                val= nums[idx] + nums[lptr] + nums[rptr]
                    
                if val==0: 
                    
                    triplet.add((nums[idx],nums[lptr],nums[rptr]))
                    lptr+=1
                    rptr-=1
                    
                    
                    while lptr<rptr and nums[lptr]==nums[lptr-1]:   lptr+=1
                    
                    
                    
                elif val>0: rptr-=1
                    
                elif val<0: lptr+=1
                    
                    
                
        for i in range(len(nums)):

            if nums[i]>0:   break

            else:   two_sum(i)


        for tup in triplet:
            res.append(list(tup))

        return res

        