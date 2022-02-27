class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        
        #Huffman Encoding
        #Sexy sawal
        
        total=0
        heapq.heapify(sticks)
            
        #print(sticks)
        
        if len(sticks)==1:  return 0
                
        while(len(sticks)!=1):
        
            combined=heapq.heappop(sticks)+heapq.heappop(sticks)
            #print(combined)
            
            total+=combined
            heapq.heappush(sticks,combined)
            
        
        return total
        