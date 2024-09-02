class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        
        s =sum(chalk)
        
        rem = k%s
        
        
        for idx,qty in enumerate(chalk):
            
            if rem<qty:
                return idx
            
            else:   rem = rem -qty
            