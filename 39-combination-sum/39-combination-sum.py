class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        ans=[]
        
        def helper(target,res,index):
            
            if target==0:
                
                val=list(res)
                val.sort()
                ans.append(val)
                return
                
            if target<0:
                return
            
            
            for i in range(0,len(candidates)):
                
                res.append(candidates[i])
                helper(target-candidates[i],res,index)     
                #removelast added/backtrack
                res.pop()
                
        
        helper(target,[],0)
        
        
        final_res=[]
        for i in ans:
            final_res.append(tuple(i))
        
        
        s=set()
        for i in final_res:
            s.add(i)
            
        #print(s)
        return list(s)