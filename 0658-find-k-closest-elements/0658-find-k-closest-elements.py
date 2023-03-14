class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        diff = []
        
        for i in range(len(arr)):
            
            heapq.heappush(diff,[abs(arr[i]-x),i])
            
            
        res=(heapq.nsmallest(k,diff))
        
        ans=[]
        for d,i in res: ans.append(arr[i])
  

        return sorted(ans)
            