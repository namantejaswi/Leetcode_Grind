class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        
        
        
        # o(n) additional linear space o(1) 
        
        p=[]
        n=[]
        

        
        for i in range(0,len(nums)):
            
            if nums[i]>=0:    
                p.append(nums[i])
            else:   
                n.append(nums[i])
           
        
        #print(n,p)
        
    
        for i in range(0,len(nums),2):
            nums[i]=p[i//2]    
                
        for i in range(1,len(nums),2):
                
            nums[i]=n[(i-1)//2]

            
            
        return nums
            
    
      
                    
        