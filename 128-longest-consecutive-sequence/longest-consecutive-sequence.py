class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        unordered_set = set(nums)
        candidates = {}
        for n in unordered_set:
            if not n-1 in unordered_set:
                candidates[n] = 1

        for start in candidates:
            i = 1
            while i < len(nums):
                if start+i in unordered_set:
                    i+=1
                else:
                    break
            candidates[start] = i
        return max(candidates.values())
        