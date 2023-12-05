class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #Brute Force O(n^3)
        
        
        res =  set()
        
        nums.sort()
        
        
        for i in range(len(nums)-1):    # for last 3
            
            lptr = i+1
            rptr = len(nums)-1
        

            while lptr<rptr:

                val = nums[i]+ nums[lptr] + nums[rptr]

                if val ==0: 
                    res.add((nums[i],nums[lptr],nums[rptr]))
                    lptr+=1      #see if theres another cobination to the right of i   
                    
                elif val<0: lptr+=1
                elif val>0: rptr-=1
                
                
        #print(res)
        ans=[]
        for tupple in res:
            ans.append(list(tupple))
            
        return ans