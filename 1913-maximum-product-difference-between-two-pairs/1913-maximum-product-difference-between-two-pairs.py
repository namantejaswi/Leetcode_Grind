class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        
        min_1 =float('inf')
        min_2 =float('inf')
        
        mx_1 = float('-inf')
        mx_2 = float('-inf')
        
        
        for n in nums:
            
            if n>mx_1:
                
                mx_2 = mx_1
                mx_1 = n
                
            else: mx_2 = max(mx_2,n)
                
                
            if n<min_1:
                
                min_2 = min_1
                min_1=n
                
            else:   min_2 = min(min_2,n)
                
                
        return (mx_2*mx_1)-(min_1*min_2)