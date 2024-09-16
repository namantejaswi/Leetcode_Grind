
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Number of missing elements before the mid position
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
    # If missing numbers are less than k, we need to search in the right part
                left = mid + 1
            else:
        # If missing numbers are greater or equal to k, search in the left part
                right = mid - 1
        
        # At the end of the loop, `left` is the position to insert the k-th missing number
        # We need to find the k-th missing number
        return left + k