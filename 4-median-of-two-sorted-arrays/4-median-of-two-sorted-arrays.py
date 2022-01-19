class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Ridiculous runnnn!
        
       
        #we apply binary search on the shorter of the array so that our 
        #time complexity is O(log(min(n,m)))
       
        if len(nums1)>len(nums2):
            
            nums1,nums2=nums2,nums1
        
        m=len(nums1)
        n=len(nums2)
        
        low=0 
        high=m
        
        
        while(low<=high):
            
            cut1=int((low+high)/2)
            cut2=int((n+m+1)/2-cut1)
            
            
            if cut1<m and nums2[cut2-1]>nums1[cut1]:
                low=cut1+1
                
            elif cut1>0 and nums1[cut1-1]>nums2[cut2]:
                high=cut1-1
                
                
            else:
 
                if cut1 == 0: max_left = nums2[cut2-1]
                elif cut2 == 0: max_left = nums1[cut1-1]
                else: max_left = max(nums1[cut1-1], nums2[cut2-1])

                if (m + n) % 2 == 1:
                    return max_left

                if cut1 == m: min_right = nums2[cut2]
                elif cut2 == n: min_right = nums1[cut1]
                else: min_right = min(nums1[cut1], nums2[cut2])

                return (max_left + min_right) / 2

                
                
                
        