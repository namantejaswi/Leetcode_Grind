class Solution:
    def passThePillow(self, n: int, time: int) -> int:
       
        
        total_trversals = time//(n-1)   #n-1 because it takes n-1 secods to reach one end to the other end 
      
        rem = time%(n-1)
        
        
        #i extra moves from starting take us to i+1
        if total_trversals%2==0: return rem+1
      
        #i extra moves from the end take us to n-rem 1,2,3,4, eg 3 move get back 4-3idx
        else: return n-rem
      