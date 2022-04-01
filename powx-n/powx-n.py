class Solution:
    def myPow(self, x: float, n: int) -> float:
        
    #To do in logn time we divide and conquer,combine
    #the negative case is taken care by just changing the form
    
        if n==0:    return 1
        
        if(n<0):
            x=1/x       #x^-n=(1/x)^n
            n=-1*n
            return self.myPow(x,n)
            
            
        div=self.myPow(x,n//2)   
        
        if(n%2==0): return div*div
        
        else: return div*div*x