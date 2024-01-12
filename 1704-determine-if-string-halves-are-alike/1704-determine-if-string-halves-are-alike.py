class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        vowels = set('aeiouAEIOU')
        for i in range(0, len(s) // 2):
            if s[i] in vowels:
                count += 1
        for i in range(len(s)//2, len(s)):
            if s[i] in vowels:
                count -= 1
        return count == 0