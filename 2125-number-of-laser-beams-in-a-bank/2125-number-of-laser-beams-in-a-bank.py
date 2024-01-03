class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = 0
        ans = 0
        for s in bank:
            count = s.count('1')
            if count > 0:
                ans += count * pre
                pre = count
        return ans
                
            