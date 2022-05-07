class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        stack=[]    #array with value and minimum
        
        mi = nums[0]
        
        
        for i in nums:
            
            while  stack and i >= stack[-1][0]:
                    
                    stack.pop()
                    
                    
            if stack and  i>stack[-1][1]:
                    
                return True
                
            stack.append([i,mi])
            mi=min(mi,i)
                    
        return False
                    