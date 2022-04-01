class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        freq={}
        s=set()
        
        for i in nums1:
        
            if i not in freq:
                freq[i]=1
                
            else:
                freq[i]+=1
                
        for j in nums2:
            
            if j in freq:
                
                s.add(j)
                
                
        return s
        
        
        
                
        