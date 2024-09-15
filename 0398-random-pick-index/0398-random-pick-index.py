class Solution:
    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, n in enumerate(nums):
            self.indices[n].append(i)

    def pick(self, target: int) -> int:
        indices = self.indices[target]
        idx = random.randrange(len(indices))
        return indices[idx]



# class Solution:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
        
#     def pick(self, target: int) -> int:
        
#         count = 0
        
#         for idx,val in enumerate(self.nums):

#             if val == target:
#                 count+=1
                
#                 #generates a random integer in the range [0, count - 1].
#                 if random.randrange(0,count)==0:
#                     picked = idx
                    
#         return picked
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)