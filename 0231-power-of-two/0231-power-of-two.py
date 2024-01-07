class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
    
    
        #A number that is a power of 2 will only only have one 1 bit in its binary rep
        
        
        if n<=0:    return False
        
        # n = n&(n-1) turns the rightmost bit off
        # a power of two will be zero after this operation
        
        
        return n & (n-1)==0
        