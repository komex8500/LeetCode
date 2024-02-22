class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans_set = set()
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                target_sum = nums[i] + nums[left] + nums[right]
                if target_sum > 0:
                    right -= 1
                elif target_sum < 0:
                    left += 1
                else:
                    target_tuple = (nums[i], nums[left], nums[right])
                    if target_tuple not in ans_set:
                        ans_set.add(target_tuple)
                        ans.append([nums[i], nums[left], nums[right]])
                    left += 1
        return ans