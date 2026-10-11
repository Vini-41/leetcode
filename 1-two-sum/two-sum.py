class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_targets = {}
        for i, num in enumerate(nums):
            potential = target-num
            if potential in seen_targets:
                return [i, seen_targets[potential]]
            else:
                seen_targets[num] = i
