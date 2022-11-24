class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        #dfs from each index as a starting index
        
        visited=set()   #local visited for each index where we move 4 directionally
                        #it stores the places we have been to starting from each idx
        def dfs(x,y,length):
            
            if length==len(word):   return True
            
            if (x,y) in visited:    return False
            
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]):     return False
            
            if  board[x][y]!=word[length]:  return False 
            
            else:
                
                visited.add((x,y))
                curr_word = dfs(x+1,y,length+1) or dfs(x,y+1,length+1) or dfs(x-1,y,length+1) or dfs(x,y-1,length+1) 
                
                visited.remove((x,y))
                return curr_word
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):

                if dfs(i,j,0):  return True
                    
        return False
            
                
                