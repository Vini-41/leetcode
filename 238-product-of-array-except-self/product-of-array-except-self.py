class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [0] * len(nums)

        answer[0] = 1
        for i in range(1, length):
            # answer[i-1] contains the product of elements to the left of i-1
            # multiply by nums[i-1] to get the product of all elements to the left of i
            answer[i] = nums[i-1] * answer[i-1]
        R = 1
        for i in reversed(range(length)):
            # R contains the product of all elements to the right of i
            # multiply answer[i] (left product) by R (right product) to get the product of everything except nums[i]
            answer[i] = answer[i] * R
            # fold nums[i] into R so it holds the product of all elements to the right of i-1
            R *= nums[i]
        return answer