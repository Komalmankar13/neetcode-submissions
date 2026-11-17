class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n =  len(nums)

        result = set()

        for item, value in enumerate(nums):
            if value not in result:
                result.add(value)
            
            else:
                return nums[item]