class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = [[] for i in range(n) ]
        indegree=[0]*n
        
        
        for e in edges:
            
            graph[e[0]].append(e[1])
            indegree[e[1]]+=1
            

        pre_req = [set() for i in range(n)]
        
        #bfs from 0 re nodes
        
        
        q = deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i) 
            
        while q:
            u = q.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                pre_req[v].add(u)
                pre_req[v].update(pre_req[u])
                if indegree[v] == 0:
                    q.append(v)


        ans = [[] for i in range(n)]
        
        for i in range(n):
            ans[i] = sorted(list(pre_req[i]))
            
        return ans
        
        
        
        
        
        
        