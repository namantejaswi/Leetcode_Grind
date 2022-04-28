class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        
        mx=0
        
        s=set()
        repeat=None
        
        for i in nums:
            if i in s:  repeat=i
            
            s.add(i)
            
            
        summation=sum(s)
        
        mx=max(s)
        
        
        if summation==mx*(mx+1)/2:
            
            return [repeat,mx+1]
        
        else:
            missing=(mx*(mx+1)/2)-summation
        

        
            return[repeat,int(missing)]