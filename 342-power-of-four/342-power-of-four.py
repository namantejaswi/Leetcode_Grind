class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        
        if n<1:    return False
        
        
        while(n>1):
            
        
            if n%4==0:
                n=int(n/4)                
                
            else:   return False
            
        return True