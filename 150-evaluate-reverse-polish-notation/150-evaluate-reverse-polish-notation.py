class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack=[]
        
        
        for i in tokens:
            
            if (i!="*" and i!= "/" and i!="+"and i!="-"):
                stack.append(int(i))
        
            if i =="+" and len(stack)>=2:
            
                stack[-2]=stack[-2]+stack[-1]
                stack.pop()
                
            if i =="*" and len(stack)>=2:
            
                stack[-2]=stack[-2]*stack[-1]
                stack.pop()
            
            if i =="-" and len(stack)>=2:
            
                stack[-2]=stack[-2]-stack[-1]
                stack.pop()
            
            if i =="/" and len(stack)>=2:
            
                stack[-2]=int(stack[-2]/stack[-1])
                stack.pop()
                        
        return stack[-1]