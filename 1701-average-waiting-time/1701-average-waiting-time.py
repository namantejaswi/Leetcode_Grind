class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        #time requred for ech ordeer + overlap
        
     
        wait_t=0
        t=0
        
        for c in customers:
            
            wait_t = max(c[0],wait_t)+c[1]
            t+=wait_t-c[0]
            
            
        return t/len(customers)
            
            