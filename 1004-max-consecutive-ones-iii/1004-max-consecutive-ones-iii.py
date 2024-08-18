class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        

        
        #problem is similar to longest non repeating substring
        
        #The problem is same as finding the longest subarray with atmost k zeros
        
        mx, curr = 0, 0
        lptr = 0
        rptr = 0
        
        n=0
        if k == 0:
            for i in range(len(nums)):
                if nums[i]==1:
                    n+=1
                    mx=max(mx,n)
                    
                elif nums[i]==0: n=0                    
            return mx
        
        for rptr in range(len(nums)):
            
            if nums[rptr] == 1:
                curr+=1  
                mx = max(curr,mx)

                
            elif nums[rptr] == 0 and k>0:
                curr+=1
                k-=1
                mx = max(curr,mx)
    
            
            elif nums[rptr]==0 and k==0:
                while lptr<rptr and k==0:
                    
                    if nums[lptr]==0:
                        k+=1
                        
                    lptr+=1
                    curr-=1
                if lptr!=rptr:  # to account for k being 0 ffrom start   
                    k-=1
                    curr+=1
                    mx=max(mx,curr)

        return mx
                
                
                
                