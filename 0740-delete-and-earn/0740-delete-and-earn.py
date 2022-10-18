class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        
        
        arr_map=defaultdict(int)
        
        
        for i in nums:
            
            if i not in arr_map:    arr_map[i]=i
            else:   arr_map[i]+=i
                
        #@    
        dic={}
        def calc(n):
            
            if n==0:    return 0 #nothing to select
            if n==1:    return arr_map[1]# we can select only 1 element
            
            
            elif n in dic:   
                return dic[n]
            
            else: 
                dic[n]= max(calc(n-1),calc(n-2)+arr_map[n])
                return dic[n]

        return calc(max(nums))
        
      
        


        

        
        
        
        