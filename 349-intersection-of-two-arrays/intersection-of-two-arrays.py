class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        ans = []
        for n in nums1:
            if n not in s:
                s.add(n)
        for n in nums2:
            if n in s:
                ans.append(n)
                s.remove(n)
        return ans