class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while right > left:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    if (nums[i], nums[left], nums[right]) not in s:
                        ans.append([nums[i], nums[left], nums[right]])
                        s.add((nums[i], nums[left], nums[right]))
                    left += 1
        return ans
