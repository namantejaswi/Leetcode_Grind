class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
                
        indegree=[[] for i in range(numCourses)]
        
        count_indegree=[0]*numCourses
        
        for  course,pre in prerequisites:
            
            indegree[pre].append(course)
            count_indegree[course]+=1
            
                
        zero_stack=[]
        
        cnt=0
        for i in range(len(count_indegree)):
            
            if count_indegree[i]==0:
                zero_stack.append(i)
            
        topo=[]
        
        while zero_stack:
            
            course_with_0_indeg=zero_stack.pop()
            cnt+=1
            topo.append(course_with_0_indeg)
            
            for i in indegree[course_with_0_indeg]:
                
                count_indegree[i]-=1
                
                if count_indegree[i]==0:
                    zero_stack.append(i)
                    
                    
        if cnt==numCourses: return topo
        
        return []