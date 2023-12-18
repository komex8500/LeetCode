
from typing import *


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        destinations = set(path[0] for path in paths)
        for start, end in paths:
            if end not in destinations:
                return end
