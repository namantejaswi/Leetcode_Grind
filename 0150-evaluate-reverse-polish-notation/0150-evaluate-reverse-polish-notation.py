class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        
        for i in tokens:
            
            if i !="*" and  i!="/" and i!="+" and i!="-":
                
                stack.append(int(i))
                
                
            else:
                
                if len(stack)>=2: #if we have 2 numbers in stack just perform operation 
                    
                    n1=stack.pop()
                    n2=stack.pop()
                    
                    if i=="+":     stack.append(n1+n2)
                        
                    elif i=="*":    stack.append(n1*n2)
                        
                    elif i=="/":    stack.append(int(n2/n1))
                    
                    elif i=="-": stack.append(n2-n1)
                        
        return stack[-1]