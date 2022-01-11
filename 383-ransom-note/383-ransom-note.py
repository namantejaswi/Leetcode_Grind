class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        dic={}
        
        for i in magazine:
            if i not in dic:    dic[i]=1
            
            else: dic[i]+=1
                
                
                
        for j in ransomNote:
            
            
            if j not in dic or dic[j]==0:    return False
            
            
            else:   dic[j]-=1
                
                
        return True