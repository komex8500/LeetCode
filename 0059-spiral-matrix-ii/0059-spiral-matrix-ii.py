
from typing import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        index = 0
        size = n - 1
        num = 1
        while num < n ** 2:
            for i in range(index, size):
                result[index][i] = num
                num += 1
            for i in range(index, size):
                result[i][-1-index] = num
                num += 1
            for i in range(index, size):
                result[-1-index][-1-i] = num
                num += 1
            for i in range(index, size):
                result[-1-i][index] = num
                num += 1
            index += 1
            size -= 1
        if n % 2 != 0:
            result[index][index] = num
        return result