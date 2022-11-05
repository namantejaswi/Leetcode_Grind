class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
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
            

        
        while zero_stack:
            
            course_with_0_indeg=zero_stack.pop()
            cnt+=1
            
            for i in indegree[course_with_0_indeg]:
                
                count_indegree[i]-=1
                
                if count_indegree[i]==0:
                    zero_stack.append(i)
                    
                    
        return cnt==numCourses
                
            
            
            
        
    