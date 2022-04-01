class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n ==1: return True
        def helper(n):
            
            
            if n/2==1:
                
                return True
            
            elif n>2:
                return helper(n/2)
            
            else: return False
                
                
        return helper(n)