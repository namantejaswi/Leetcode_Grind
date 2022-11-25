class Solution:
    def numSteps(self, s: str) -> int:
        
        
        
        n=int(s,2)
        
        if n==1:    return 0
        
        steps=0
        
        while n!=1:
            
            
            if n%2==1:
                
                n+=1
                steps+=1
                
                
            elif n%2==0:
                n=n//2
                steps+=1
                
        return steps
        