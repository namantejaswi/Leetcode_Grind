class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        
        
        size=len(nums)
        
        if size<3:  return []
        
        
        nums.sort()
        
        ans=set()
        
        for i in range(size):
            
            
            lptr=int(i+1)    # we take i,lptr and rptr
            rptr=int(size-1)
            
            
            while(lptr<rptr):
                
                curr=nums[i] + nums[lptr]+nums[rptr]
                
                if curr==0:
                    ans.add((nums[i],nums[lptr],nums[rptr]))
                    lptr+=1

                elif curr>0:
                    rptr-=1
                elif curr<0:
                    lptr+=1
                    
                    
       # print(ans)
                
        for i in ans:
            i=list(i)
            
        ans=list(ans)
        
        
        for i in  range(len(ans)):
            ans[i]=list(ans[i])
            
        return(ans)        
    
    