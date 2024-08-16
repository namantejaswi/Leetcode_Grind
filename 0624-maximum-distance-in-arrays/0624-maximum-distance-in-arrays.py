class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        mi_so_far = arrays[0][0]
        mx_so_far = arrays[0][-1]
        
        
        max_delta = float('-inf')
        
        
        for i in range(1, len(arrays)):
            
            delta_1 =abs( arrays[i][-1] - mi_so_far)
            delta_2 = abs(mx_so_far - arrays[i][0])
            max_delta= max(max_delta,delta_1,delta_2)
            
            mi_so_far = min(mi_so_far,arrays[i][0])
            mx_so_far = max(mx_so_far,arrays[i][-1])
            
            
        return max_delta
            
            
            