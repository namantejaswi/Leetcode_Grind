class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        
        heap_arr=[]
        
        l=len(matrix)
        
        
        for i in range (min(l,k)):
            
            
            heap_arr.append((matrix[i][0],i,0))
            
            
        heapq.heapify(heap_arr)
        
        while k:
            
            num,i,cnt=heapq.heappop(heap_arr)
            
            if cnt<l-1:
                heapq.heappush(heap_arr,(matrix[i][cnt+1],i,cnt+1))
            
            k-=1
                
        return num