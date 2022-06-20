class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        
        visited=set()
        
        
        def dfs(i,j,ch):
            
            if ch==len(word):   #we have meet the word and at next recursive call return true
                return True
            
            if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                return False
            
            if (i,j) in visited:    return False
            
            if board[i][j]!=word[ch]:    return False
            
            else:
                
                visited.add((i,j))
                found= dfs(i+1,j,ch+1) or dfs(i,j+1,ch+1) or dfs(i-1,j,ch+1) or dfs(i,j-1,ch+1)
                visited.remove((i,j))
                return found
                
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if dfs(i,j,0):  return True
                
        return False
            
            
        