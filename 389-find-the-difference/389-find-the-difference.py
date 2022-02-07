class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        freq_map={}
        
        for i in s:
            if i not in freq_map:
                freq_map[i]=1
                
            else:   freq_map[i]+=1
            
         
        for j in t:
            
            if j not in freq_map:   return j
            if j in freq_map:
                
                if freq_map[j]==1:
                    del freq_map[j]
                    
                    
                else:   freq_map[j]-=1
                    
                   
        return freq_map.keys()
                    
                    
                    