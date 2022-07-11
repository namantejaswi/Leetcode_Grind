class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        
        mx=-1
        
        for i in (accounts):
            
            mx=max(mx,sum(i))
            
            
        return mx