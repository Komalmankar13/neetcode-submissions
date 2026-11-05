class Solution:
    def sortColors(self, nums: List[int]) -> None:
        start = 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == 0:
                nums[start], nums[left] = nums[left], nums[start]
                left += 1
                start += 1
            
            elif nums[left] == 1:
                left += 1

            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1