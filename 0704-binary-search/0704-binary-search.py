from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while right >= left:
            index = (left + right) // 2
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                return index
        return -1