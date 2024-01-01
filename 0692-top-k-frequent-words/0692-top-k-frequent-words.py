class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        
        freq={}
        
        for w in words:
            
            if w in freq:   freq[w]+=1
                
            else:   freq[w]=1
                
        
        res=[]
        
        for key,val in freq.items():
            
            res.append([key,val])
            
        res.sort(key = lambda x:(-x[1],x[0]))   #sort by freq and lexo for tie
        

        ans =[]        
        cnt=0
        for i in range(k):   
            ans.append(res[i][0])
            
            
        return ans