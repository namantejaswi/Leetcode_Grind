class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        
        cnt=0
        
        flag=0
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                
                if board[i][j]=="X":
                    
                    #we count at top left if its either 0 or is the first block i.e nothing in previous row or column

                    if((i>0 and board[i-1][j]=="X") or (j>0 and board[i][j-1]=="X")):
                        
                        continue
                    
                    cnt+=1
        return cnt
                
                