class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
    
    #Key idea: All the permuations are same when sorted
    
        dic = {}
        
        for word in strs:
        
            sorted_word=''.join(sorted(word))
            
            #we use sorted_word as the key
            
            if sorted_word  in dic:
                 dic[sorted_word].append(word)
                
            else:      
                dic[sorted_word]=[word] #missed the damm[]  1 hour wasted ffs                  
                
              
        print(list(dic))
        res=[]
        for v in dic.values():    res.append(v)
            
        return res
                
