class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def get_mapped_value(num):
            if num == 0:
                return mapping[0]
            mapped = 0
            factor = 1
            while num:
                mapped += mapping[num % 10] * factor
                num //= 10
                factor *= 10
            return mapped

        # Create a list of tuples: (original number, mapped value, original index)
        mapped_nums = [(num, get_mapped_value(num), i) for i, num in enumerate(nums)]
        
        # Sort based on mapped value, then original index
        mapped_nums.sort(key=lambda x: (x[1], x[2]))
        
        # Return the sorted original numbers
        return [x[0] for x in mapped_nums]