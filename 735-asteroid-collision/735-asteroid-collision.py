class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        
        
        stack=[]
        
        #Any negative asterodid starting or a sequence of -ve asteroid
        #starting will never collide with anything and any end with positive
        #or consequtive positive end will not collide with any thing
    
        # for collison we first need a positive direction and a negative
        
       
        for i in range(len(nums)):
        
            #when do we have a collision
        
            while stack and stack[-1] > 0 and nums[i]<0:
                
                
                delta = stack[-1] + nums[i]
                
                if delta>0:
                    
                    #i.e positve element in stack is greater 
                    #negative incoming elment is destroyed, dont do anything                    
                    nums[i]=0   #we wont add element with value zero
                    
                elif delta<0:
                    stack.pop()
                
                else:
                    stack.pop()
                    nums[i]=0
                    
                #flag tells when do we not add the -ve element
                    
            if nums[i]!=0:
                stack.append(nums[i])
                
        return stack   
                
                
                
                
                
                
                
                
                
                
                
                
        
        
        
        