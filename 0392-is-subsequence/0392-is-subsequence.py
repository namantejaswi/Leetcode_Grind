class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        if len(t)<len(s):   return False
        
        if len(s)==0:   return True
        if len(t)==0:   return False
        
        ptr_s=0
        ptr_t=0
        
        
        
        for i in range(len(t)):
            
            if s[ptr_s]==t[ptr_t]:
                
                if ptr_s==len(s)-1:  return True     #we have reached the end
                
                else:
                    ptr_s+=1
                    ptr_t+=1
            else:
                
                ptr_t+=1
                