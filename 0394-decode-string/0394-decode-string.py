class Solution:
    def decodeString(self, s: str) -> str:
        
        
        stack=[]
        
        curr_string=""
        
        curr_num=0
        
        for i in range(len(s)):
            
            if s[i]=='[':
                
                stack.append([curr_string,curr_num])
                curr_string=""
                curr_num=0
                
            elif s[i]=="]":
                
                prev_string,num=stack.pop()
                curr_string=prev_string+(num*curr_string)
                
            elif s[i].isdigit():
                curr_num=10*curr_num+int(s[i])           #if we have 2 digit or longer numbers
                
            else:   curr_string+=s[i]
                
        return curr_string
    
    

    