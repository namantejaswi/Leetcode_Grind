class Solution:
    def totalMoney(self, n: int) -> int:
        
        
        total=0
        last=0
        
        
        for i in range(0,n):
                  
            if i!=0 and i%7==0: 
                last=last-5
                total+=last                
                
            else:
            
                last+=1
                total+=last
        return total
            
                
        
            