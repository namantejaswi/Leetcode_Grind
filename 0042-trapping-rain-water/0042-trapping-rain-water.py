class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        
        #we can make an optimization so that we have to use only O(1) space instead of O(n) linear space 
        
        
        
        
        left, right = 0, len(height)-1
        mx_l = height[left]
        mx_r = height[right]
        
        #if single element
        if left==right: return 0
        
        total = 0
        
        while(left<right):
            
            if mx_l < mx_r:
                
                left+=1
                mx_l = max(mx_l,height[left])
                
                total += max(0, mx_l-height[left])
        
            else:
                
                right-=1
                mx_r = max(mx_r,height[right])
                total+=max(0, mx_r-height[right])
                
        return total
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #we try to calculate the water trapped by each index
        #water trapped by each index is limited by the largest element to the left and right , min(max_to_the_left,max_to the_right)-h
        
#         max_to_left = [0 for i in range(len(height))]
#         max_to_right = [0 for j in range(len(height))]
        
#         mx_l = height[0]
#         mx_r = height[-1]
        
        
#         for i in range(1,len(height)):
        
#             max_to_left[i] = mx_l
#             mx_l = max(mx_l,height[i])
            
            
#         for j in range(len(height)-2,-1,-1):
#             max_to_right[j] = mx_r
#             mx_r = max(mx_r, height[j])
        
#         total = 0
        
#         for h in range(len(height)):
            
#             total += max(min(max_to_left[h],max_to_right[h])-height[h], 0)
            
#         return total
            