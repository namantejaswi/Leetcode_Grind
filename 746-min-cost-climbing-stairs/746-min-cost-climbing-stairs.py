class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        dp=[-1]*(len(cost)+1)
        
        def calc(idx):
            
            if dp[idx]!=-1: return dp[idx]   
            
            elif idx<=1:  
                dp[idx]=0
                #since we can start at zero or one the minimum cost is zero
                
                return dp[idx]
            
            
            else:
                
                dp[idx]=min(calc(idx-1)+cost[idx-1],calc(idx-2)+cost[idx-2])
                return dp[idx]
            
            
        return calc(len(cost))
    
