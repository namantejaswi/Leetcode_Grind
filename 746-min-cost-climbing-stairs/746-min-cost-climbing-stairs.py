class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        #dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-1])
        #base case dp[0]=cost[0],dp[1]=cost[1]
        
        #stupid question top floor or target is one index ahead of last elment in arr
        
        dp=[-1]*(len(cost)+1)
        def calc(idx):
            if idx<=1:  #becase we can start from one or zero
                dp[idx]=0
                return dp[idx]
                        
            elif dp[idx]!=-1: return dp[idx]
        
            else:
                
                dp[idx]=min(calc(idx-1)+cost[idx-1],calc(idx-2)+cost[idx-2])
                return dp[idx]
                
        calc(len(cost))
        return dp[-1]