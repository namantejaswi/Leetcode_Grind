class Solution:
    def isArmstrong(self, n: int) -> bool:
        
          
    
        if n <=9: return True
        total = 0
        
        num =n
        k=0
        arr = []
        
        while num>9:
            k+=1
            arr.append(num%10)
            num = num//10  
            
        k+=1    
        arr.append(num)
        print(arr,k)
    
        for i in arr: total = total + (i)**k
            
        return total ==n