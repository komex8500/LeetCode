class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = dict()
        ans = 0
        for n1 in nums1:
            for n2 in nums2:
                if n1+n2 in d:
                    d[n1+n2] += 1
                else:
                    d[n1+n2] = 1
        for n3 in nums3:
            for n4 in nums4:
                if -n3-n4 in d:
                    ans += d[-n3-n4]
        return ans