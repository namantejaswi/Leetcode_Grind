class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        def helper(s1,s2):
            mx=0
            dp=[[0 for x in range(len(nums1)+1)] for y in range(len(nums2)+1)]
            
            for i in range(len(s1)):
                for j in range(len(s2)):
                    if(s1[i]==s2[j]):
                        dp[i][j]=1+dp[i-1][j-1]
                        mx=max(dp[i][j],mx)              
                 
            
            #print(dp[-1][-1]) initially the last row and colum are zero
            #but not a good practice to write this way lol 
            return mx

        return helper(nums1,nums2)
        
        