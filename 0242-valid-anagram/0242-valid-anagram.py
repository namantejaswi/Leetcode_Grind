class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        import math
        cnt=0
        
        prime = [2]
        
        def is_prime(x):
            
            root = sqrt(x)
            
            for i in range(2,math.ceil(x)):
                
                if x%i==0:  return False
                
                
            return True
        
        
        for i in range(3,150):
            
            if len(prime)==26:  break
                
            else:
                
                if is_prime(i)==True: prime.append(i)
                    
        #print(prime,len(prime))
        
        dic = dict()
        cnt=0
        for i in range(97,97+26):
            
            dic[chr(i)]=prime[cnt]
            cnt+=1
            
        #print(dic)
        
        p1=1
        p2=1
        
        
        for ch in s:   
            p1 = p1*dic[ch]
            
        for ch in t:
            p2=p2*dic[ch]
            
            
        return p1==p2
        
        
        
        