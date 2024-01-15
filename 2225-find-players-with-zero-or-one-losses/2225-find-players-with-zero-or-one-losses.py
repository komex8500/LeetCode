class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_dict = dict()
        ans1 = []
        ans2 = []
        for i in range(len(matches)):
            lose_dict[matches[i][0]] = lose_dict.get(matches[i][0], 0)
            lose_dict[matches[i][1]] = lose_dict.get(matches[i][1], 0) + 1
        for c in sorted(list(lose_dict.keys())):
            if lose_dict[c] == 0:
                ans1.append(c)
            elif lose_dict[c] == 1:
                ans2.append(c)
        return [ans1, ans2]