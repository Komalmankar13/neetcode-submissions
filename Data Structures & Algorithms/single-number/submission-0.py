class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newList = {}

        for num in nums:
            if num in newList:
                newList[num] += 1
            else:
                newList[num] = 1
        
        for item, value in newList.items():
            if value == 1:
                return item
        