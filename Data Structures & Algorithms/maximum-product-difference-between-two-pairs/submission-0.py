class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        minimum = nums[left] * nums[left + 1]
        maximum = nums[right] * nums[right - 1]

        difference = maximum - minimum

        return difference
        