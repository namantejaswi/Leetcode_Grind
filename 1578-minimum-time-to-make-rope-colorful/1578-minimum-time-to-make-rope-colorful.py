class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        last=0
        total=0
        for i in range(1,len(colors)):
            
            if colors[last]!=colors[i]:
                last=i
                
            else:
                total+=min(neededTime[i],neededTime[last])
                if neededTime[i]>neededTime[last]:
                    last=i            

        return total
        
                     
    #sexy sawal