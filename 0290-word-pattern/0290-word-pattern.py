class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        
        dic={}
        words=s.split(" ")
        
        
        if len(words)!=len(pattern):    return False
        
        
        for i in range(len(pattern)):
            
            
            
            if pattern[i] not in dic:
                dic[pattern[i]]=words[i]
                
            elif pattern[i] in dic:
                if dic[pattern[i]]!=words[i]:return False
  

        return len(set(dic.keys()))==len(set(dic.values()))

        #return True