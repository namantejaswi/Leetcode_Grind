class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        
        cnt=0
        
        
        freq={}
        
        for i in words1:
            
            if i not in freq:
                freq[i]=1
                
            else:   freq[i]+=1
                
                
        d2={}
        
        for w in words2:
            if w not in d2:
                d2[w]=1
            else:   d2[w]+=1
        
        for j in words2:
                
            if j in freq and d2[j]==1 and freq[j]==1:
                cnt+=1
                
                
        return cnt