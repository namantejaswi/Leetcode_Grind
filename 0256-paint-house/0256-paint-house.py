class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        
        if not costs: return 0
        
        dp=[[-1 for i in range(3)]for j in range(len(costs))]
        
        #dp[n][i], where i=0,1,2 represents the min cost of painting nth row with ith color 
        
        
        def calc(n,color):
        
            if dp[n][color]!=-1:    return dp[n][color]
        
        
            curr_cost=costs[n][color]
        
            
            if n==len(costs)-1:  return curr_cost    #if at last house 
            
            else:
                
                if color==0: curr_cost+=min( calc(n+1,1), calc(n+1,2))
                    
                if color==1: curr_cost+=min( calc(n+1,0), calc(n+1,2))
                    
                if color==2: curr_cost+=min( calc(n+1,0), calc(n+1,1))
                
                dp[n][color]=curr_cost
                return curr_cost
                
                
        return min(calc(0,0),calc(0,1),calc(0,2))
                
                
                
                
                
            
            
            
            