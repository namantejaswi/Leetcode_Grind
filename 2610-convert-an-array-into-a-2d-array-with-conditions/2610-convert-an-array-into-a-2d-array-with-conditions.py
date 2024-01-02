class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        
        freq={}
        
        for i in nums:
            if i in freq:   freq[i]+=1
            else:   freq[i]=1
                
        res=[]  
        cnt=0
        
    
        while cnt<len(nums):
            arr=[]
            for k,v in freq.items():
                if freq[k]>0:
                    arr.append(k)
                    freq[k]-=1
                    cnt+=1


            res.append(arr)
            
            
        return res