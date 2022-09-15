class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        
        if len(changed)%2==1:   return []
        
        res=[]

        freq={}
        
        
        for i in changed:
            if i not in freq:
                freq[i]=1
                
            else:   freq[i]+=1
                
                     
        changed.sort()
        res=[]
        
        for i in changed:

            if freq[i]>0:
                
                freq[i]-=1
                
                if 2*i not in freq or freq[2*i]==0:
                    
                    return []
                
                elif freq[2*i]>0:   
                    freq[2*i]-=1
                    
                    #print("found double of",i)
                    res.append(i)
                    
        return res