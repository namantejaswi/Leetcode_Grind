class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        
        
        max_l=0
        stack=[]
        stack.append(-1)

        for i in range(len(s)):
            
            if s[i]=='(':
                stack.append(i)
                
            else:
                
                stack.pop()
                if len(stack)==0:   stack.append(i)
                    
                else:
                    current_l=i-stack[-1]
                    max_l=max(max_l,current_l)
            
        
        return max_l

            
        
        #if len(s)==0:   return 0
        
        #dp=[0 for i in range(len(s))]
        
       
        #max_l=0
        #counter=0
        #dp[0]=0
        #for i in range(len(s)):
            
         #   if s[i]=="(":    
          #      counter +=1
           #     dp[i]=dp[i-1]
                
            #if s[i]==")" and counter<=0:
             #   dp[i]=0
            
            #elif s[i]==")" and counter>0:    
                
             #   counter-=1
              #  dp[i]=dp[i-1]+2
                
        
        #print(dp)
        #return(max(dp))
            