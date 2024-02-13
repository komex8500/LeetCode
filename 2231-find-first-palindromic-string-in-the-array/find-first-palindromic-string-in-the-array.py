class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i = 0
            j = len(word)-1
            while j > i:
                if word[i] != word[j]:
                    break
                i += 1
                j -= 1
            if word[i] == word[j]:
                return word
        return ""
