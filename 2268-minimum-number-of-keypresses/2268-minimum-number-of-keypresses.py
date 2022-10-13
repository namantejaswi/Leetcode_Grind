class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        
        freq={}
        
        
        for i in range(len(s)):
            
            if s[i] in freq:    freq[s[i]]+=1
                
            else:   freq[s[i]]=1
                
        
        f=dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        
        count=0
        res=0
        for i in f:
            
            if count<9:
                res+=f[i]*1
                count+=1
                
            elif count>=9 and count <18:
                res+=2*f[i]
                count+=1
                
            else:   
                res+=f[i]*3
                count+=1
        return res
