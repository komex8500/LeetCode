class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        um = {}
        for i in nums:
            um[i] = um.get(i, 0) + 1
        
        ans = []
        while um:
            temp = []
            to_erase = []
            for f, s in um.items():
                temp.append(f)
                s -= 1
                if s == 0:
                    to_erase.append(f)
                um[f] = s
            ans.append(temp)
            for i in to_erase:
                del um[i]
        return ans