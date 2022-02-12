class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #sexy sawal 
        
        if len(s1)>len(s2):
            return False
        
        hash_s1={}
        window={}
        
        for i in s1:
            
            if i not in hash_s1:

                hash_s1[i]=1
                    
            else:   hash_s1[i]+=1
                
                
        
        for i in range(len(s1)):
            if s2[i] not in window:
                window[s2[i]]=1
                
            else:   window[s2[i]]+=1
                
        if window==hash_s1:  return True     #the starting of s2 is same as s1 
        
        
        #now we take our first window in s2 of size s1  and slide
        #it over the entire second string
        
        
        for i in range(0,len(s2)-len(s1)):
            
            if window[s2[i]]==1:
                del window[s2[i]]
                
            else:   window[s2[i]]-=1
                
                
            if s2[i+len(s1)] not in window:
                window[s2[i+len(s1)]]=1
                    
            else:   window[s2[i+len(s1)]]+=1
                
            if window==hash_s1:  return True        
        
            
        return False
            
            
            
            
            
            
            