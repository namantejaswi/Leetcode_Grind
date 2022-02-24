class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        flips=0

        for i in range(len(s)):
            
            
            if s[i]=="1":
                count+=1
                   
            else:
                flips+=1
                
            flips=min(count,flips)
            
        return flips