class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        to_visit=set()
        for i in range(0,len(rooms)):    to_visit.add(i)
    
        visited=set()
        
        q=deque()
        q.append(0)
        
        while q:
            
            
            r_idx = q.pop()

            
            for i in rooms[r_idx]:
                
                for j in [i]:
                    
                    if j in visited:    continue
                    
                    else:
                        visited.add(j)
                        to_visit.remove(j)
                        q.append(j)
        
        if 0 in to_visit:to_visit.remove(0)
        return len(to_visit)==0