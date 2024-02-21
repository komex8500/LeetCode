class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        left_b = bin(left)
        right_b = bin(right)
        if len(left_b) != len(right_b):
            return 0
        b = ''
        for i in range(2, len(left_b)):
            if left_b[i] == right_b[i]:
                b += str(left_b[i])
            else:
                b += '0'*(len(left_b)-i)
                break
        return int(b, 2)