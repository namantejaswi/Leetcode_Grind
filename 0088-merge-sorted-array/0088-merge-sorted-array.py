class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        #to make use of the zeos at the end we choose the largest array
        
        
        ptr1=m-1
        ptr2=n-1
        idx=m+n-1
        
        while ptr1>=0 and ptr2>=0:
            
            if nums1[ptr1]>nums2[ptr2]:
                
                nums1[idx]=nums1[ptr1]
                idx-=1
                ptr1-=1
                
            else:
                nums1[idx]=nums2[ptr2]
                idx-=1
                ptr2-=1
           
                
        if ptr1<0:
            
            
            nums1[:ptr2+1]=nums2[:ptr2+1]
            
        
            
            
            
        