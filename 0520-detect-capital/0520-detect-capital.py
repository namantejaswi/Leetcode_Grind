class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        
        
        #0 for small 1 for caps
        first_w=0
        
        def is_small(char):
            
            return (ord(char)>=97 and ord(char)<=122)
        
        count_caps=0
        count_small=0

        
        for i in range(1,len(word)):

            
            if is_small(word[i]) and count_caps>0:  return False
            
            if not is_small(word[i]) and count_small>0: return False
            
            else:
                if is_small(word[i]):   count_small+=1
                else:   count_caps+=1
            
                    
        if count_caps==0 or count_small==len(word)-1:    return True #all small first can be small or large 
        
        if count_caps==len(word)-1 and not is_small(word[0]): return True 
        
        