class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(text):
            l, r = 0, len(text) - 1
            while r > l:
                text[l], text[r] = text[r], text[l]
                l += 1
                r -= 1
            return text

        arr = list(s)
        for i in range(0, len(s), 2*k):
            arr[i:i+k] = reverse(arr[i:i+k])

        return "".join(arr)