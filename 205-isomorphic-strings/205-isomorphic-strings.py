class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    
        if len(s)!=len(t):  return False
        
        dic={}
        
        for i in range(len(s)):
            
            
            #if the second str char is already mapped to something else
            
            if s[i] not in dic and t[i] in dic.values():
                
                return False
            
            
             #if the first str char is mapped to something else already
            elif s[i] in dic and dic[s[i]]!=t[i]:
                
                return False
            
            #if both of the chars are not in dic we add them and
            #map them to one another    
            
            elif (s[i] not in dic and t[i] not in dic.values()):
                
                dic[s[i]]=t[i]
            
            
        return True
            
                