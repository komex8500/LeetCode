class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        vowels = set('aeiouAEIOU')
        for i in range(len(s)):
            if s[i] in vowels:
                if i < len(s) // 2:
                    count += 1
                else:
                    count -= 1
        return count == 0