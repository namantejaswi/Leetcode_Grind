class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        
        #the largest odd number will be the one with right most odd digit
        
        idx = None
        
        for i in range(len(num)):
            
            if (int(num[i]))%2==1:
                
                idx = i
                
        if idx is None:     #careful cant use not idx since 0 index
            return ""
        
        return (num[:idx+1])