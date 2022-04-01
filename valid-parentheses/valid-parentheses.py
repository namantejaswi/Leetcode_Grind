class Solution:
    def isValid(self, s: str) -> bool:
        
        
        
        #we have 2 types of brackets opening and closing 
        #For a valid paranthesis 
        #we want that for the last opening bracket the first closing bracket is same
        
        #We use stack as its Lifo, we push the opening braces on top of the stack
        #and then pop as we find the closing braces by making sure they are the same           #and the stack is not empty
        
        close_open={')':'(','}':'{',']':'['}
        stack=[]
        
        for ch in s:
            
            if ch in close_open.values():    #ch is opening 
                
                stack.append(ch)
                
            elif(stack and stack[-1]==close_open[ch]):        
               
            #stack is not empty and last element or the top elemnt is equal to
            #corresponding closing pair we have in our dict
         
                stack.pop()        
                
            else:
                return False
            
        return(not(len(stack)))     #true if our stack is empty
        
