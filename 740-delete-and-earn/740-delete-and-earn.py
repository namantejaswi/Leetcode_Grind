class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        
        
        
        dic=defaultdict(int)
        
        for i in nums:
            if i not in dic:
                dic[i]=i
            else:   dic[i]+=i
                
        
        @lru_cache
        def mx_point(n):
            
            if n==0:    return 0
            if n==1:    return dic[1]
                
            return max(mx_point(n-1),mx_point(n-2)+dic[n])
            
        return mx_point(max(nums))
           