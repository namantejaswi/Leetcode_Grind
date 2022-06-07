class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        
        
        res=[0]*len(temp)
       
        stack=[]
    
        for i in range(len(temp)):
            
            if len(stack)==0:
                stack.append([temp[i],i])
                      
            else:
          
                while stack and stack[-1][0]<temp[i]:
                    prev=stack.pop()
                    res[prev[1]]=i-prev[1]
        
            stack.append([temp[i],i])
            
        #print(stack)
                    
        return res
            
        