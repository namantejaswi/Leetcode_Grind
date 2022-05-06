class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        #bandhiyan sawal
        
        stack=[[None,None]]   #First element stores the elment the second count
        
        
        for i in s:
        
            if i == stack[-1][0]:
                stack[-1][1]+=1
                
                if stack[-1][1] == k:
                    
                    stack.pop()
                    
                    
            else:   stack.append([i,1])
        
        
        #print(stack)
        
        res=""
        
        for i in range(1,len(stack)):
            
            res+=stack[i][0]*stack[i][1]    #append the letter count times
            
            
        return res
            
        