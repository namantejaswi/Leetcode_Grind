class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        
        res=""
        
        if numerator%denominator == 0:  

            return str(numerator//denominator)  #to avoid unecessary .0
        
        
        if numerator*denominator <0:  res+="-"
            
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        q,remainder = divmod(numerator,denominator)
        res+= str(q)
        
        seen_remainder = {}
        
        
        decimal=""
        idx=0
        while remainder>0 and remainder not in seen_remainder:
            
            seen_remainder[remainder] = idx
            idx+=1
            
            q,remainder = divmod(remainder*10, abs(denominator))
            decimal+=str(q)
            
        #If we have a repeating deciaml i.e. remainder    
        if remainder in seen_remainder:     
            
            idx=seen_remainder[remainder]
            return res+  '.' + decimal[:idx] + '(' + decimal[idx:] + ')'
        
        else: return res+"."+decimal[:]
            
            
            
            
        