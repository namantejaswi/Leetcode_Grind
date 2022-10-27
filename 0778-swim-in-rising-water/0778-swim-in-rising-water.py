class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
         

        mx=0
        l=len(grid)
        visited=set()
        heap=[] #we add value,x,y
        visited.add((0,0))
        heap.append([grid[0][0],0,0])
        
        
        while heap:
            
            elem=heapq.heappop(heap)
            
            lvl=elem[0]
            x=elem[1]
            y=elem[2]
            
            mx=max(mx,lvl)
            
            if x==l-1 and y==l-1:   return mx
        
            for i,j in ((x+1,y),(x-1,y),(x,y+1) ,(x,y-1)):
                
                if i>=0 and i<l and j>=0 and j<l and (i,j) not in visited:
                    
                    heapq.heappush(heap,[grid[i][j],i,j])
                    visited.add((i,j))
            
            
            
            
        
            
            
            
        
#         mi= float("inf")
#         l=len(grid)
#         w=len(grid[0])
#         orignal=[[0 for i in range(l)] for j in range (l)]
#         for i in range(l):
#             for j in range(l):
#                 orignal[i][j]=grid[i][j] 
#         print("orignal",orignal)   

#         def dfs(x,y,time,temp_grid):

#             nonlocal mi
#             if x>=l or y>=w or x<0 or y<0 or temp_grid[x][y]==-1:  
#                 return 
#             #cant move
#             if temp_grid[x][y] > time:   
#                 print("current value exceede's Time",time)
#                 return 

#             temp_grid[x][y]=-1
            
#             if x==l-1 and y==w-1:    
#                 mi=min(mi,time)
#                 print("voila reached final destination")
#                 return
#             else:        
#                 dfs(x-1,y,time,temp_grid)
#                 dfs(x,y-1,time,temp_grid)
#                 dfs(x+1,y,time,temp_grid)
#                 dfs(x,y+1,time,temp_grid)

        
#         for t in range(0,max(max(grid))+1):
#             # grid=orignal
#             temp_grid=orignal
#             print("grid",grid)
#             print("orignal",orignal)
#             # print(t,grid)
#             dfs(0,0,t,orignal)
            
#         return mi
        
    
    
    
    
    
        