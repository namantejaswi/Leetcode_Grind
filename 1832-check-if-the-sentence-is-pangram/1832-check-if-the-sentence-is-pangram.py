class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        
        s={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
        
        for i in sentence:
            
            if i in s:
                s.remove(i)
                
                
        return len(s)==0