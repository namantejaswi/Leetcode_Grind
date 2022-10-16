class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
        
        stack=[]
        
        lower_bound=float("-inf")
        
        
        
        for i in preorder:
            
            if i <lower_bound:  return False
            
            
            else:
                
                while stack and i>stack[-1]:
                    
                    lower_bound=stack.pop()
                
                stack.append(i)
                
        return True