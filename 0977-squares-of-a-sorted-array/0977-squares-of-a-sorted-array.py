
from typing import *

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [float('inf')] * len(nums)
        left, right, index = 0, len(nums) - 1, len(nums) - 1
        while right >= left:
            if nums[left] ** 2 > nums[right] ** 2:
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return result