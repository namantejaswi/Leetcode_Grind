class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        
        freq = dict()
        for i in arr:   
            if i in freq:   freq[i]+=1
            else:   freq[i]=1
                
        # instead of sorting we push no. and frequencies into min heap and pop smaller freq first
        #freq = dict(sorted(freq.items(), key = lambda x:x[1]))
        
        heap = []
        
        for key,val in freq.items():
            
            heap.append( [val,key]) #heapify does not take keyword like key and by deafult heapifies based on first element
            
            
        #print(heap)
        
        
        heapq.heapify(heap)
        while heap and k!=0:
            
            count = heapq.heappop(heap)#heappop maintains heap invariant i.e heapifies
            
            if count[0]<=k:
                
                k=k-count[0]
                #heapq.heapify(heap) heap pop maintains heap invariant
            
            elif count[0]>k:
                
                heapq.heappush(heap,[count[0]-k,count[1]])
                k=0
                                     
        #print(heap)
        
        return len(heap)
                
                
            
            
            
            
        
        
        