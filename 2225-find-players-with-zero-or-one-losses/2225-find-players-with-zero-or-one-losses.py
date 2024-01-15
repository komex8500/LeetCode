class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_dict = dict()
        lose_dict = dict()
        ans1 = []
        ans2 = []
        for i in range(len(matches)):
            win_dict[matches[i][0]] = win_dict.get(matches[i][0], 0) + 1
            lose_dict[matches[i][1]] = lose_dict.get(matches[i][1], 0) + 1
        for c in sorted(list(win_dict.keys())):
            if c not in lose_dict:
                ans1.append(c)
        for c in sorted(list(lose_dict.keys())):
            if lose_dict[c] == 1:
                ans2.append(c)
        return [ans1, ans2]