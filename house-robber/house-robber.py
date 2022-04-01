class Solution:
        def rob(self, nums: List[int]) -> int:
    
            l=len(nums)-1
            cache=[0]*len(nums)

            
            if l<0: return 0
        

            cache[0]=0
            
            if(l==0):
                cache[0]=nums[0]
            if (l==1):     
                cache[1]=max(nums[1],nums[0])
            
            #Bottom up iterative approach
            #Recurssive formula
            
            #f(0)=0, f(1)=max(f(0),nums[1])

            #f(n)=max(f(n-2)+nums[n],f(n-2))
            
            if(l>1):
            
                for i in range(len(nums)):
                    cache[i]=max(cache[i-2]+nums[i],cache[i-1])
            
            return(cache[l])
        
'''
#Recurrsive Bottom up with memoization

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        l=len(nums)-1
        
        self.cache=[-1]*len(nums)
        
        return(self.count(nums,len(nums)-1))

        
    def count(self,nums, l):

        if l<0: return 0

        if(self.cache[l]>-1):    return self.cache[l]

        else:       

            curr= max(self.count(nums,l-2)+nums[l],self.count(nums,l-1))
            self.cache[l]=curr
            return curr

'''