# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        
        
        
        l=1
        r=n
        while(l<=r):
            
                        
            mid=(l+r)//2
            g=guess(mid)
            if g==0:
                return mid
            
            if g==1:
        
                l=mid+1
            
            else:
                r=mid-1
                
                
        return -1
        