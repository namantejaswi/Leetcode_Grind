class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        res=[]
        
        s1=set(nums1)
        
        
        for n in nums2:
            if n in s1: 
                res.append(n)
                s1.remove(n)
                
        return res