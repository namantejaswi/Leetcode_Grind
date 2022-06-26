class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        
        '''
        #correct top down dp solution
        lptr=0
        rptr=len(nums)-1
        res=0
        if len(nums)==1:    return nums[0]

        cache={}
        def choose(lptr,rptr,k):
            
            if lptr>rptr:
                return 0

            if k==0: return 0
            
            else:
                k-=1
            
                if (lptr,rptr) in cache:
                    return cache[(lptr,rptr)]
                else:
                    cache[(lptr,rptr)]=max(nums[lptr]+choose(lptr+1,rptr,k),nums[rptr]+choose(lptr,rptr-1,k))
        
                return cache[(lptr,rptr)]
             
        return choose(lptr,rptr,k)'''
        
        
        #find the min sub array of length we remove it and get the maximum length of sub array
        l=0
        r=len(nums)-k-1
        s=sum(nums[:r+1])

        mi=s
        
        for i in range(r+1,len(nums)):
           
            s+=nums[i]-nums[l]
            if s<mi:
                mi=s
            
            l+=1
         
        return sum(nums)-mi