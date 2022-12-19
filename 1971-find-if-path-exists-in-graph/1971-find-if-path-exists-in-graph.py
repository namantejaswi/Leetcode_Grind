class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        if source == destination: return True
        
        outdeg=[set() for i in range(0,n)]
        for path in edges:
            #non directional graph
            outdeg[path[0]].add(path[1])
            outdeg[path[1]].add(path[0])
         
        
        #we perform bfs to determine of we can reach that path
        
        
        q=deque()
        
        visited=set()# we only add those neighbours whose elements have been explored
        
        if not outdeg[source]:  return False
        
        for i in outdeg[source]:    
            q.append(i)
            visited.add(source)
        
                
        while q:
            
            node=q.pop()
            if node in visited: continue
            
            if node==destination:   return True
            
            for i in outdeg[node]:  
                q.append(i)
            
            visited.add(node)
                
                
        return False
            
            
            
            
            
            
        
        
        
        
        