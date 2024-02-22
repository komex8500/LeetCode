class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [0] * n
        b = [0] * n
        for i in range(len(trust)):
            a[trust[i][0]-1] += 1
            b[trust[i][1]-1] += 1
        if 0 in a:
            judge = a.index(0)
            return judge + 1 if b[judge] == n-1 else -1
        else:
            return -1