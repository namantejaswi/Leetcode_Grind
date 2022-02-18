class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        #opening_bracket_not_closed
        left_open=0
        not_closed=0
        
        stack=[]
        
        for i in range(len(s)):
            
            if  s[i]==")":
                if len(stack)==0:
                    not_closed+=1
                else:   stack.pop()
                
            elif s[i]=="(":
                stack.append(s[i])
                 
                 
        return len(stack)+not_closed
            
                