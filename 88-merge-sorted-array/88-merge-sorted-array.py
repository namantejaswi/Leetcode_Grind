class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ptr1=m-1
        ptr2=n-1
        
        #To do it inspace we take advantage of the padded zeros by starting 
        #from the end
        
        while(ptr1>=0 and ptr2 >=0):
            
            if nums1[ptr1]>nums2[ptr2]:
                nums1[ptr1+ptr2+1]=nums1[ptr1] #+1 as both index start from 0
                ptr1-=1
                
            else:
                nums1[ptr1+ptr2+1]=nums2[ptr2]
                ptr2-=1
        print(ptr1,ptr2,nums1)  
        
        #if elements remain num2        
        if ptr2>ptr1:
            nums1[:ptr2+1]=nums2[:ptr2+1]
            
        #if elements remain in num1 no need to do anything    
        
            
        
    
        
        
        