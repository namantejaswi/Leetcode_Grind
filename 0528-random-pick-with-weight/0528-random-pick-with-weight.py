class Solution:

    def __init__(self, w: List[int]):
        
        
        self.running_sum=[]
        rs=0
        for wt in w:
            rs+=wt
            self.running_sum.append(rs)
        self.total_sum=rs
        

    def pickIndex(self) -> int:
        
        r=random.random()*self.total_sum
        lo=0
        hi=len(self.running_sum)
        while lo < hi:
            mid = (lo + hi)// 2
            if r > self.running_sum[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()