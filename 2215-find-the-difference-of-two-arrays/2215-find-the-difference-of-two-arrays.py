class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        
        
        
        d1={}
        d2={}
        
        
        for i in nums1:
            
            if i not in d1:
                d1[i]=1
                
            else:   d1[i]+=1
                
                
        for i in nums2:
            
            if i not in d2:
                d2[i]=1
                
            else:   d2[i]+=1
                
                
        p1,p2=[],[]
                
            
        for i in set(nums1):
            
            if i not in d2:
                
                p1.append(i)
                
        for i in set(nums2):
            
            if i not in d1:
                
                p2.append(i)
                
                
        return [p1,p2]