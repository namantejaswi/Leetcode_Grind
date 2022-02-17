class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        ans=[]
        
        def helper(target,res):
            
            if target==0:
                
                val=list(res)
                val.sort()
                ans.append(val)
                return
                
            if target<0:
                return
            
            
            for i in range(len(candidates)):
                
                res.append(candidates[i])
                helper(target-candidates[i],res)     
                #removelast added/backtrack
                res.pop()
                
        
        helper(target,[])
        #print(ans)
        
        final_res=[]
        for i in ans:
            final_res.append(tuple(i))
        
        
        s=set()
        for i in final_res:
            s.add(i)
            
        #print(s)
        return list(s)