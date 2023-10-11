class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        
        flowers.sort(key = lambda x:x[0])
        
        heap = []
        
        dic_count = {}
        
        sorted_people = sorted(people)
        
        idx = 0
        
        for p in sorted_people:
        
            while idx<len(flowers) and flowers[idx][0]<=p:#flower blooms before arrival
            
                heapq.heappush(heap,flowers[idx][1])
                idx+=1
                
            while heap and heap[0]<p:
                heapq.heappop(heap)
                
            dic_count[p] = len(heap)     #no. of flowers the person will see
                
        
        return [dic_count[i] for i in people]