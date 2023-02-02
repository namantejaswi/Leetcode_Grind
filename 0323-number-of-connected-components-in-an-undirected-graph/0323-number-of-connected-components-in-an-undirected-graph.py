class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        
        visited = set()
        
        
        graph=[set() for i in range(n)]
        
        
        for e in edges:
            
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])
            
        #print(graph)

        
        component = 0
        
        
        def dfs( node_number):
            
            for adj in graph[node_number]:
                if adj not in visited:
                    visited.add(adj)
                    dfs(adj)
            
        
        for node in range(n):
            
            if node not in visited:
                dfs(node)
                component+=1
                
                
        return component
                
                