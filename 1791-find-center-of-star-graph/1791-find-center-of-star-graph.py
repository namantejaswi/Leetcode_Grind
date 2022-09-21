class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        a=edges[0]
        b=edges[1]
        
        if a[0] in b:   return a[0]
        else:   return a[1]
            