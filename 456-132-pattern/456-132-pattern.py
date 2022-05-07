class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        stack=[]    #array with value and minimum so far
        
        mi = nums[0]
        
        
        for i in nums:
            
            while  stack and i >= stack[-1][0]:
                    
                    stack.pop()
            
            #we maintain a stack such that we have the biggest element on top and while storing the biggest element we also have the smallest element which occured previous to the bigger as we append the variable mi as previous min
            
            
            if stack and i<stack[-1][0] and i>stack[-1][1]:
                
            
                return True
                
            stack.append([i,mi])
            mi=min(mi,i)
                    
        return False
                    