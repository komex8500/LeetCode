class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)//2):
            l[i], l[-1-i] = l[-1-i], l[i]
        return " ".join(l)