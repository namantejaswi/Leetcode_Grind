class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
        total = 0
        x,y = startPos[0], startPos[1]
        
        if x<homePos[0]:    total+=sum(rowCosts[x+1:  homePos[0]+1])
        
        elif x>homePos[0]:  total+=sum(rowCosts[homePos[0]:x])
            
        if y<homePos[1]:    total+=sum(colCosts[y+1:   homePos[1]+1])
            
        elif y>homePos[1]:  total+=sum(colCosts[homePos[1]:y])
            
        return total