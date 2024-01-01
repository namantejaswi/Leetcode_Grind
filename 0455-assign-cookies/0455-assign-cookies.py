class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        
        s.sort()
        g.sort()
        
        
        cnt=0
        
        size_ptr=0
        greed_ptr=0
        
        while greed_ptr<len(g) and size_ptr<len(s):

            if s[size_ptr]>=g[greed_ptr]:
                cnt+=1
                size_ptr+=1
                greed_ptr+=1
                
            else:   
                size_ptr+=1
                
                
        return cnt
                
        
        
        
        