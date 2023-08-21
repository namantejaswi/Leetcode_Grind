class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        #if a substring can be used to repeat the entire string
        #then the length of the substring divides the length of the string w/o rem
        
        
        l = len(s)
         
        for i in range(1,l//2+1):   #max length of sub is l/2
            
            
            if l % i ==0:
                
                subs = s[:i]
                
                if s == subs * (l//i):  return True
            
        return False