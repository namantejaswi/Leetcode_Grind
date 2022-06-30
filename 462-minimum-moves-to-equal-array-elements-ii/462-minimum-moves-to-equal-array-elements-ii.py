class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        s=sum(nums)
        median=None
        identity_elem=None
        
        if len(nums)%2==0:
      
            
            p1=nums[int((len(nums)/2)-1)]
            p2=nums[int(len(nums)/2)]
            
            if abs(s-(p1*len(nums)))<(abs(s-(p2*len(nums)))):
                identity_elem=p1
                
            else:
                identity_elem=p2
                
            #print(identity_elem)
            
            
        else:
            identity_elem = nums[int(len(nums)//2)]
            
            
        res=0
            
        for i in nums:
            res+=abs(i-identity_elem)

        return res