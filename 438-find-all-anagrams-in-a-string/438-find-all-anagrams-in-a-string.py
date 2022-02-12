class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        

        if len(p)>len(s):
            return []
        
        res=[]
        
        map_1={}
        
        for i in p:
            
            if i not in map_1:
                map_1[i]=1
                
                
            else:
                map_1[i]+=1
                
        window_size=len(p)
        
        #initialize initial window
        window={}
        
        for i in range(0,window_size):
                
                if s[i] not in window:
                    window[s[i]]=1
                    
                else:   window[s[i]]+=1
        
        if window==map_1:   res.append(0)    
        
        for i in range(0,len(s)-window_size):
            
            if window[s[i]]==1:
                del window[s[i]]
                    
            else:   window[s[i]]-=1
                    
            if s[i+window_size] in window:
                
                window[s[i+window_size]]+=1
                
            else:   window[s[i+window_size]]=1
            
            if window==map_1:   res.append(i+1)
            
                
        return res        
                
                    
        