class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        
        #DFS plus meomization
        
        
        #Brute force dfs O(4^n)  if m==n 4^n
        
        #we can reduce exponential time complexity to polynomial time complexity
        #by memoization to avoid recomputing overlapping subproblem
        
        
        memo = {}
        
        #memo of i,j stores the longest path starting at index i,j
        #so if we call dfs(i,j,prev) and i,j in memo we can straight away return 
        
        #also increasing path is always a dag it cant connect to same elment
        
        def dfs(x,y,prev):
            
            nonlocal memo
            
            if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0]) or matrix[x][y]<=prev:  return 0 
            
            
            if (x,y) in memo: return memo[(x,y)]
            
            
            else:
                
                left = dfs(x-1,y,matrix[x][y])
                right = dfs(x+1,y,matrix[x][y])
                up = dfs(x,y+1,matrix[x][y])
                down = dfs(x,y-1,matrix[x][y])
                
                
                #every cell intself is a increasing path of length 1
                memo[(x,y)] = 1+max(left,right,up,down)    
                return memo[(x,y)]
                
                
        res=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                
                res = max(res, dfs(i,j,float('-inf')))
                
        print(memo)
                
        return res
                
                
        
                
                
                
        
                
            
        