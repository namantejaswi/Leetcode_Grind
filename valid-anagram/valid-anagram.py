class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s)!=len(t)): return False
        
        c_map={}
        
        
        for i in s:
            if i not in c_map:
                c_map[i]=1
            
            else:   c_map[i]+=1
                
                
                
        for j in t:
            if j not in c_map or c_map[j]==0:
                return False
                
            else:   c_map[j]-=1
                
                
        return True