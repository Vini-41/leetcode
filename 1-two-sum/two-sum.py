class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            desired_value = target - num
            if desired_value in seen:
                return [seen[desired_value], i]
            seen[num] = i