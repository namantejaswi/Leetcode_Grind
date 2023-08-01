class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        #Total combination is nCk
        
        
        def helper(start_index, combination ):
        
            if len(combination)==k: 
                res.append(combination[:])
                return
        
            for i in range(start_index,n+1):

                combination.append(i)
                helper(i+1,combination)
                combination.pop()


        helper(1,[])
        
        return res