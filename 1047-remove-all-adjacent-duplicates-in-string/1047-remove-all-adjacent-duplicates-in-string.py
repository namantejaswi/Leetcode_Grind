class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        #use stack if top == current element pove andmove ahead
        
        
        stack=[]
        
        
        for i in range(len(s)):
            
            if len(stack)==0:
                
                stack.append(s[i])
                
                
           
            elif s[i]!=stack[-1]:
                #print("aapneding",s[i])
                stack.append(s[i])
                    
            elif s[i]==stack[-1]:
                #print("poppping",stack[-1])
                stack.pop()
                    
                    
                    
        return ("".join(stack))
        
        