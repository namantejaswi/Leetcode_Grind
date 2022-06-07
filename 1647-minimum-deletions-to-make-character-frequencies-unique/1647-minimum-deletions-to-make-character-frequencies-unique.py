class Solution:
    def minDeletions(self, s: str) -> int:
        
        
        freq_map={}
        
        s=list(s)
        
        for i in s:
            if i in freq_map:   
                freq_map[i]+=1
            else:   
                freq_map[i]=1
                
                
        cnt={}
        
        for k,v in freq_map.items():
            
            if v in cnt:
                cnt[v].append(k)
                
            else:   cnt[v]=[k]
                
        cnt=dict(sorted(cnt.items()))
        
        #print(cnt)
        
        res=0
        s2=set()
        for k,v in cnt.items():
            while len(cnt[k])>1:
                char=cnt[k].pop()
                
                f=k
                
                while((f in cnt or f in s2) and f>0 ):
                        f=f-1
                        res+=1
                
                if f>0:
                    s2.add(f)
            
    
        return res
        
            