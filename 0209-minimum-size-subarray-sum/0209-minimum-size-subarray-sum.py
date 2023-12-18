
from typing import *


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = len(nums)
        sum, result = 0, float('inf')
        left, right = 0, 0
        while right < l:
            sum += nums[right]
            while sum >= target:
                result = min(result, (right - left + 1))
                sum -= nums[left]
                left += 1
            right += 1
        return 0 if result == float('inf') else result