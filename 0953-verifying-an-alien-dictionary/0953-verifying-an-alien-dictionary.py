class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        
        dic={}
        
        for index,alpha in enumerate(order):
            
            dic[alpha]=index+1
            
        
        
        for i in range(len(words)-1):
            
            
            for j in range(len(words[i])):
                
                #if next word is same until the end and longer
                if len(words[i+1])<=j:   return False
                
                
                #words are not same
                if words[i][j]!=words[i+1][j]:
                    #weightage of index of second graett than first word smae idx
                    if dic[words[i][j]]>dic[words[i+1][j]]:
                        return False
                
                #if not the words are sorted no need to continue to check remaningn
                
                    else:   break
                
                
        return True
                