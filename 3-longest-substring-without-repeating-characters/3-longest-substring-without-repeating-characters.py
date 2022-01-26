class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        c_set=set()
        max_l=0
        
        left=0
        
     
        for end in range(len(s)):
            
            while s[end] in c_set:
                c_set.remove(s[left])
                left+=1
                
            
            c_set.add(s[end])
            max_l=max(max_l,end-left+1)
            
        return max_l