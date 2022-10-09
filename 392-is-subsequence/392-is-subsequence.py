class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        if s=="":    return True
        if t=="":    return False
        s=list(s)
        t=list(t)
        
        ptr1=0
        ptr2=0
        
        for i in range(len(t)):
            
            
            
                
            
            if s[ptr1]==t[ptr2]:
                
                if ptr1==len(s)-1:    return True
                else:
                    ptr1+=1
                    ptr2+=1
               
            else:   ptr2+=1
            