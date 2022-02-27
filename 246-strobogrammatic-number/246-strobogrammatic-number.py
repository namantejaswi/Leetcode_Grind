class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        rotated={'0':'0','1':'1','6':'9','8':'8','9':'6'}
        
        
        left=0
        right=len(num)-1
        

        while(left<=right):
            
            if num[right] not in rotated or num[left] not in rotated or num[right]!=rotated[num[left]]:
                return False
            
            left+=1
            right-=1
            
        return True
            
