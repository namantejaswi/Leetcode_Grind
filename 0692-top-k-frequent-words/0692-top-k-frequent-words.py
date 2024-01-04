class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        
                
        dic={}
        
        
        for i in words:
            
            if i not in dic:
                dic[i]=1
                
            else:   dic[i]+=1
                
        
        #we heapify the frequency
        
        arr = [[-freq,word] for word,freq in dic.items()]

        #print(arr)
        
        #python only has min heap so we multipy frquency by -1 to have largest frequency on top of the heap
        
        heapq.heapify(arr)
        
        res=[]
        
        while(len(res)!=k):
            
            res.append((heapq.heappop(arr)[1]))
            
            
        return res
        
        
        
        
        