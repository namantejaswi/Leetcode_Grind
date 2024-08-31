class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()  # Sort the ages in ascending order
        total_requests = 0
        n = len(ages)

        def binary_search_left(target, end):
            left, right = 0, end
            while left < right:
                mid = (left + right) // 2
                if ages[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search_right(target, start):
            left, right = start, n
            while left < right:
                mid = (left + right) // 2
                if ages[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1

        for i in range(n):
            if ages[i] <= 14:  # This accounts for age[y] <= 0.5 * age[x] + 7 when age[x] <= 14
                continue

            min_age = ages[i] // 2 + 7  # Calculate minimum age to whom this person can send requests
            left = binary_search_left(min_age, i)
            right = binary_search_right(ages[i], i)

            if right >= left:
                total_requests += right - left

        return total_requests
