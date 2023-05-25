class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        g.sort()
        s.sort()
        s=deque(s)
        
        
        cnt=0
        index=0
        while(index<len(g)):
        
            if not s:   return cnt
            
            curr = s.popleft()
            
            if curr>=g[index]:
                cnt+=1
                index+=1
                
                
        return cnt
                
                