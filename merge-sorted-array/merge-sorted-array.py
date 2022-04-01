class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        p1=m-1
        p2=n-1
        
        if m==0 and n!=0:
            nums1[:]=nums2[:]
            return(nums1)
        if m==0 and n==0:
            return nums1
        if m==0 and n==0:
            return([])
        
        while(p1>=0 and p2>=0):
            
            
            if(nums1[p1]>=nums2[p2]):
                nums1[p1+p2+1]=nums1[p1]
                p1-=1
                
            elif(nums2[p2]>nums1[p1]):
                nums1[p1+p2+1]=nums2[p2]
                p2-=1
            
        if(p1<0 and p2>=0):
            nums1[:p2+1]=nums2[:p2+1]
        
        return nums1