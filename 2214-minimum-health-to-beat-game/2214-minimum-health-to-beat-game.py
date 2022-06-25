class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
        
        s=sum(damage)
        mx=max(damage)
        
        if armor>=mx:  return s-mx+1
        else: return s-armor+1
        