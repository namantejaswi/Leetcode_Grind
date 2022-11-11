class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        
        
        l=len(image)
        w=len(image[0])
        visited=set()
        
        target=image[sr][sc]
        
        def dfs(i,j):
            
            
            if i<0 or j <0 or i>=l or j>=w or (i,j) in visited or image[i][j]!=target:
                return
            
            else:
                
                visited.add((i,j))
                if image[i][j]==target:  image[i][j]=color
                    
            
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                

        dfs(sr,sc)
                        
        return image