class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        freq={}
        
        st=list(s)
        
        for i in st:
            if i not in freq:
                freq[i]=1
                
            else:   freq[i]+=1       
        
        #We use the most frequent character first and second most next repeadtedly!
        #we use an heap to keep track of the most frequent character
        
        arr=[]
        
        for k,v in freq.items():
            arr.append([-v,k])  #by default heapify works with first index
        #print(arr)
        
        heapq.heapify(arr)
        
        
        res=""
        prev=None
        
        while arr or prev:      #either we have something in the heap or we have something in prev
            
            
            #if we have a previous element but our heap is empty
            if prev and not arr:
                return ""
            
            if arr:
                elem=heapq.heappop(arr)
                elem[0]+=1      ##decrease count min heap all -ve so +1
                res+=elem[1]
            
            if prev!=None:
                heapq.heappush(arr,prev)
                prev=None
                
            
            if elem[0]!=0:  #count is -ve in our min heap i.e. actually +ve
                prev=elem
                
        return res
                
                
                
                
                
                
            
            
        
        
        
        
        
        