class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        costs.sort(key = lambda x:-abs(x[0]-x[1]))
    
        
        count_a=0
        count_b=0    
        res=0
        n=len(costs)//2
        
        for i in range(len(costs)):
            if costs[i][0]<costs[i][1]:
                count_a+=1
                res+=costs[i][0]                
                
            elif costs[i][0]>=costs[i][1]:
                count_b+=1
                res+=costs[i][1]
                
            if count_a==n and count_b!=n:
                for j in range(i+1,len(costs)):
                    res+=costs[j][1]
                    count_b+=1
                break
                
            if count_b==n and count_a!=n:
                for k in range(i+1,len(costs)):
                    res+=costs[k][0]
                    count_a+=1
                break
                
                
        return res
                
                
        
        