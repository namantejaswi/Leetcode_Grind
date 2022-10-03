class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        time,last=0,0
        for i in range(1,len(colors)):
            if colors[i]!=colors[last]:
                last=i
                
            else:
                time+=min(neededTime[i],neededTime[last])
                
                
                #if removing previous is easier we remove previous
                #and set last to curr
                if neededTime[i]>neededTime[last]:  last=i  
                
                #else we let previous be last and remove curr
        
        return time
    
    
    
    