class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
    
        s=list(s)
        
        stack=[]
        
        to_remove=set()
        
        for i in range(len(s)):
            
            if s[i]=="(":
                stack.append(i)
                
            elif s[i]==")":
                if len(stack)!=0:
                    stack.pop()
                else:   
                    to_remove.add(i)
                    
                    
        #print(s)
        for i in range(len(stack)):
            to_remove.add(stack[i])
            
            
        #print(to_remove)
        
        res=""
        for i in range(len(s)):
            if i not in to_remove:
                res+=s[i]
                
        return res
        