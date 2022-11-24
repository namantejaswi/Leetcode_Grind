class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        
        f1=dict(Counter(word1))
        f2=dict(Counter(word2))        
        
        
        for w in f1.keys():
            
            if f1[w]<=3 and w not in f2: continue
                
            elif f1[w]>3 and w not in f2:   return False
            
            elif w in f1 and w in f2 and abs(f1[w]-f2[w])>3: return False
            
        for w2 in f2.keys():
            if f2[w2] >3 and w2 not in f1:  return False
        
        
        return True