class Solution:
    def intervalIntersection(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        ptr1=0
        ptr2=0
        
        res = []
        
        while ptr1<len(nums1) and ptr2<len(nums2):
            
            
            #-------
            #   -------
            # start is max(start1,start2)
            # end is min(end1,end2)
            # overlap if start<=end
            
            lo = max(nums1[ptr1][0],nums2[ptr2][0])
            hi = min(nums1[ptr1][1],nums2[ptr2][1])
            
            if lo<=hi:
                res.append([lo,hi])
                
            #Now every time we will increase the ptr for the interval which ends earlier since it wont overlap but the later interval can still overlap
            
            if nums1[ptr1][1]<nums2[ptr2][1]:
                ptr1+=1
            
            else:   ptr2+=1
                
                
        return res
            
                       