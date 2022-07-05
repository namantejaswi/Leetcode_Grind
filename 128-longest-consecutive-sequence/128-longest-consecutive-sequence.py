class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        s=set(nums)
        
        mx_l=0
        for i in s.copy():
            
            l=0
            n=i
            n2=i
            while(n-1 in s):
                l+=1
                s.remove(n-1)
                #print("removed",n-1)
                n-=1
                
            while(n2+1) in s:
                l+=1
                s.remove(n2+1)
                #print("removed",n2+1)
                n2+=1
                
            if i in s:  s.remove(i)
            l+=1    #for element itself
            mx_l=max(l,mx_l)
            
        return mx_l
            