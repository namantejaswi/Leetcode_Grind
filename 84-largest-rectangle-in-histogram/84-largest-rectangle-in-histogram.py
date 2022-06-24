class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        #The basic idea is any rectangle starting from any index of max area will be when you extend from the ceiling of the current bar in both direction, we can continue extending until we have a smaller element to the left or the right
        
        #once we have the smaller element on bith sides we calulate the area of the biggest rectangle we can have centered around current index and compare it with the global max.
        
        #now finding the next smallest elment to left and right can be done in n^2 trivially but we see that there is some amount of overlap of work, we can actually use a stack and calulate the previous smaller element and the next smaller element beforehand for all index!
        
        mx=0
        
        
        #next smallest
        stack=[]
        ans=[[-1,-1]]*len(heights)
        #print(ans)
        for i in range(len(heights)-1,-1,-1):
            
            if len (stack)==0:  ans[i]=[-1,-1]
                
            elif heights[i]>stack[-1][0]:
                ans[i]=stack[-1]
            
               
            while(stack and stack[-1][0]>=heights[i]):
                stack.pop()

            if len(stack)==0:   
                ans[i]=[-1,-1]

            elif stack[-1][0]<heights[i]:
                ans[i]=stack[-1]

            stack.append([heights[i],i])                
        #print("next smaller",ans)
            
                
        #Previous smaller elment
        
        stack=[]
        res=[[-1,-1]]*len(heights)
        
        for i in range(len(heights)):
            
            if len (stack)==0:  res[i]=[-1,-1]
                
            elif heights[i]>stack[-1][0]:
                res[i]=stack[-1]
            
               
            while(stack and stack[-1][0]>=heights[i]):
                stack.pop()

            if len(stack)==0:   
                res[i]=[-1,-1]

            elif stack[-1][0]<heights[i]:
                res[i]=stack[-1]

            stack.append([heights[i],i]) 
            
        #print("previous smaller",res)
        
                
        if len(heights)==2: 
            return max(min(heights)*2,max(heights))
            
        for i in range(len(heights)):
            
            if ans[i][0]!=-1 and res[i][0]!=-1:
                w=ans[i][1]-res[i][1]-1
                #print("width",w,"height",heights[i])    
                mx=max(mx,(heights[i]*w))
                    
                
            elif ans[i][0]==-1 and res[i][0]==-1:
                mx=max(mx,len(heights)*heights[i])
                
                
            elif ans[i][0]==-1 and res[i][0]!=-1:
                #previous smallest exist but next does not
                
                r=len(heights)-1
                w=r-res[i][1]
                #print("here,",i,w,w*heights[i])
                mx=max(mx,w*heights[i])
                
                
            elif ans[i][0]!=-1 and res[i][0]==-1:
                #next smallesr exist but previous does not
                l=0
                r=ans[i][1]
                w=r-l
                mx=max(mx,w*heights[i])
                    
                
        
                
                
                
            
            
                
                    
        return (max(mx,max(heights)))
        
        
        