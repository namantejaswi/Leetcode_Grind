class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        
        
        w_map={}
        
        for i in range(len(wordsDict)):
            
            w_map[i]=wordsDict[i]
            
            
        d1,d2=999999,9999999
        d_min=9999999
        for i in range(len(w_map)):
            if w_map[i]==word1:
                d1=i
                
            if w_map[i]==word2:
                d2=i
                
            if abs(d1-d2)<d_min:
                d_min=abs(d1-d2)
            
        return d_min