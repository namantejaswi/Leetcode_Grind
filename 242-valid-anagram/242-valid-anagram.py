class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        dic={}
        if len(s)!=len(t):  return False
        for i in s:
            
            if i in dic:    dic[i]+=1
                
            else:   dic[i]=1
                
                
        for j in t:
            
            if j not in dic or dic[j]==0:    return False
            
            else:   dic[j]-=1
                
                
        return True