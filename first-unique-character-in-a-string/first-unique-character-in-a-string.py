class Solution:
    def firstUniqChar(self, s: str) -> int:
              
        c_map={}
        
        for i in s:
            if i not in c_map:
                c_map[i]=1
                
            else:   c_map[i]+=1
                
        
        x=[]
                
        for key,val in c_map.items():
            if val==1:  
                x=key
                break
                
                
        for i in range(len(s)):
            if s[i] ==x:
                return i
            
        return -1
                
                
    
            
