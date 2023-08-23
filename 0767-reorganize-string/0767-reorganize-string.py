class Solution:
    def reorganizeString(self, s: str) -> str:
        
        
        #We follow a greedy approach where we try to use the most frequent characters
        #alternately and update it
        
        
        
        freq = dict(Counter(s))
        #print(freq)
        
        #python only has min heap so we add char and negative of freq , also we add
        #freq first since the heap property by default of array is based of zero index
        
        arr =[]
        
        for k,v in freq.items():    arr.append([-v, k])
                    
        heapq.heapify(arr)
        
        res = ""
        prev = None
        
        #previous keeps the elment we added to our res and are looking for the next
        #char
        
        while arr or prev:
            
            
            if prev and not arr:    return ""#cant make 
            
            
            if arr:   
                
                curr = heapq.heappop(arr)
                curr[0]+=1
                res += curr[1]
        
            
            if prev!=None: 
                heapq.heappush(arr,prev)
                prev=None
        
            if curr[0]!=0:  prev=curr
                
                
        return res  
                
            #the order here is tricky we first check if we have at least something in the heap, because prev represnts the last element used, then if we have something in the heap we pop it and decrease its frequeny, now at this point it is possible we have a previous so we push previous at set prev to curr given that count >0
                
                
                
                
        
        
            
            
            
            
            
            
        
            
            
        
        
        
        
        
        
        