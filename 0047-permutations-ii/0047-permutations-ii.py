class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
    
    
        res=set()
        
        l=len(nums)
        
        def dfs(path, used):
            
            
            
            if len(path)==l:    
                res.add(tuple(path[:]))
                return
            
            else:
                for i in range(len(nums)):
                    if used[i]==True: continue
                        
                    else:
                        path.append(nums[i])
                        used[i]=True
                    
                        dfs(path,used)
                        path.pop()
                        used[i]=False
                    
                    
        dfs([],[False]*l)
        return res
            