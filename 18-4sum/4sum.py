class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = set()
        ans = []
        nums.sort()
        for j in range(len(nums)-3):
            for k in range(j+1, len(nums)-2):
                left = k+1
                right = len(nums)-1
                while left < right:
                    total = nums[j] + nums[k] + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        if (nums[j], nums[k], nums[left], nums[right]) not in s:
                            ans.append([nums[j], nums[k], nums[left], nums[right]])
                            s.add((nums[j], nums[k], nums[left], nums[right]))
                        left += 1
        return ans