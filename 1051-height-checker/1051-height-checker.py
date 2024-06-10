class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        h = sorted(heights)
        
        cnt = 0
        for i in range(len(heights)):
            
            if heights[i]!=h[i]:    cnt+=1
                
        return cnt