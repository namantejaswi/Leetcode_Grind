class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        
        ransom_note={}
            
        for i in ransomNote:
            if i not in ransom_note:
                    ransom_note[i]=1
            elif i in ransom_note:
                ransom_note[i]+=1
                 
        mag={}
                    
        for i in magazine:
            if i not in mag:
                mag[i]=1
                    
            else:   mag[i]+=1
        
        
        for i in ransomNote:
            
            if i not in mag:return False
            if i in mag:
                if mag[i]==0:   
                    return False
                else:   mag[i]-=1
                    
        return True
        