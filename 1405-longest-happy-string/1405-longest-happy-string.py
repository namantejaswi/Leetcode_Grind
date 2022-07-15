class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        
        
        res=""
        
        heap=[]
        
        
        if a!=0:heapq.heappush(heap,(-a,"a"))
        if b: heapq.heappush(heap,(-b,"b"))
        if c: heapq.heappush(heap,(-c,"c"))
        
        while heap:
            
            ch=heapq.heappop(heap)
            char=ch[1]
            count=ch[0]
            
            if len(res)>1 and res[-1]==res[-2] and res[-1]==char:
                if not heap:    return res
          
                else:
                    ch2=heapq.heappop(heap)
                    char2=ch2[1]
                    count2=ch2[0]

                    res+=char2
                    count2+=1
                        
                    if count2!=0:   heapq.heappush(heap,(count2,char2))
                        
            else:
                res+=char
                count+=1
            if count!=0:
                heapq.heappush(heap,(count,char))
                        
        return res  
                        
                
                    