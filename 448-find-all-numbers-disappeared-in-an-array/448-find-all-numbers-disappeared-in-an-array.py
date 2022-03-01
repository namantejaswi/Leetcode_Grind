class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=set(nums)
        mx=len(nums)
        res=[]
        for i in range(1,mx+1):
            if i not in s:
                res.append(i)
            
        return res
            