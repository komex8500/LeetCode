class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        list1 = [0] * 26
        list2 = [0] * 26
        for i in range(len(word1)):
            if word1[i] not in word2:
                return False
            list1[ord(word1[i]) - ord('a')] += 1
            list2[ord(word2[i]) - ord('a')] += 1
        list1.sort()
        list2.sort()
        return list1 == list2