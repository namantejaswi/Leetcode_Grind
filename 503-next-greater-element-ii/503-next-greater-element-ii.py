class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        
        
        n=len(nums)        
        stack=nums[::-1]
        ans=[-1]*n
        
        #classic next greater problem but we have a circular array so we add the nums in reverse into the stack before starting out so that we have the additional elments to look at i,e the elements to the left there is still some overhead as we are also appending the elements of to the right of a particular elment but we wont reach it since the would already have been considered before reaching here
        
        for i in range(n-1,-1,-1):
            
                            
            while(len(stack)>0 and stack[-1]<=nums[i]):
                stack.pop()
                
            if len(stack)==0:
                ans[i]=-1
                
            elif stack[-1]>nums[i]:
                ans[i]=stack[-1]
                
            stack.append(nums[i])
            
        return ans
    
    
    