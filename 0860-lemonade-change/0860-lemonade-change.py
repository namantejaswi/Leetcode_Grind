class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = [0,0,0]  #5,10,15
        
        for i in bills:
            
            if i ==5:   
                change[0]+=1
                
            elif i == 10:
                
                if change[0]<=0:
                    
                    return False
                
                else:
                    change[0] -= 1
                    change[1] +=1 
                    
            elif i == 20:
                
                if change[1] >=1 and change[0]>=1:
                    
                    change[0] -= 1
                    change[1] -=1
                    
                elif change[0]>=3:
                    change[0] -= 3
                
                else: return False
                    
        return True
                    
                    
                    
            
                    
                    