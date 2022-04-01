class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        
        #To store the number of prereq for each course
        indegree=[0]*numCourses
        
        
        #To store the courses to which this course servers a prereq and is required
        #this so that when we complete a course we can update the indegree of that 
        
        
        needed=[[] for i in range(numCourses)]
        
        for cur,req in prerequisites:
            needed[req].append(cur)
            indegree[cur]+=1
            
        stack=[]
        count=0
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                stack.append(i) #Value at ith index represents no of prereq for i
                
        
        while (stack):
            
            zero=stack.pop(0)
            count+=1
            
            for c in needed[zero]:
                indegree[c]-=1
                
                if indegree[c]==0:  
                    stack.append(c)
                    
                    
        return count==numCourses
                    
                    
            
            
            
            
            
            
            
        
            