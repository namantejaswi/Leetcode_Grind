class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
       
        
        print(ord("A"),ord("Z"))
        print(ord("a"),ord("z"))
        
        large=0
        small=0
        
        for i in range(len(word)):
            
            if ord(word[i])<=90:
                large+=1
                
            elif ord(word[i])>=97:
                small+=1
            
        #print(small,large)
        
        for i in range(len(word)):
            
            if ord(word[i])<=90 and i!=0 :
                
                if small!=0:
                    return False
            
            
        return True