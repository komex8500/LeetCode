class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        dict1 = dict()
        dict2 = dict()
        for i in range(len(word1)):
            dict1[word1[i]] = dict1.get(word1[i], 0) + 1
            dict2[word2[i]] = dict2.get(word2[i], 0) + 1
        if dict1.keys() != dict2.keys():
            return False
        list1 = list(dict1.values())
        list2 = list(dict2.values())
        return sorted(list1) == sorted(list2)