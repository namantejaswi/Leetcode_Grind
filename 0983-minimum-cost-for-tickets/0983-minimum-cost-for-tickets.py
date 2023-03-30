class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        dp = [0]*366
        
        travel_days = set()
        
        for d in days:  travel_days.add(d)
                    
        
        for i in range(1,366):  #days are indexed from 1 to 365
            
            
            if i not in travel_days:    dp[i]=dp[i-1]
                
            else:
                
                one_day = dp[i-1]+costs[0]
                seven_day = dp[max(i-7,0)]+costs[1]
                thirty_day = dp[max(i-30,0)]+ costs[2]
                
                dp[i] = min(one_day,seven_day,thirty_day)
                
        
        return dp[-1]