class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        #Adjacency List reppresentation outgoing edges that is the courses it seves a  pre req to 
        
        adj_list= {}
        
        for i in range(numCourses):
            adj_list[i]=[]
            
        for i in prerequisites:
            adj_list[i[1]].append(i[0])
        
        #print(adj_list)
         
        #sort by indegree i.e lowest number of pre req    
        #pre_req=dict(sorted(pre_req.items(), key=lambda x: len(x[1])))
        
        pre_req={}
        for i in range(numCourses):
            pre_req[i]=[]
            
        for i in prerequisites:
            pre_req[i[0]].append(i[1])
        
        indegree=[-1]*numCourses
        
        for i in range(numCourses):
            indegree[i]=len(pre_req[i])
        #print(indegree)
        
        q=deque([])
        topological_order=[]
        
        for i in range(len(indegree)):
            if indegree[i]==0:    
                q.append(i)
                
        if not q: return[]
        
        while(q):
            node=q.popleft()
            #print(node)
            topological_order.append(node)
            
            outgoing=adj_list[node]
            for i in outgoing:
                #print(indegree)
                indegree[i]-=1
                if indegree[i]==0:  
                    q.append(i)
                    
                    
        if len(topological_order)!=numCourses:  return []
        
        return topological_order
            
            
        
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        