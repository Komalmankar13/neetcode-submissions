class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        
        duplicates = []
        for key, value in d.items():
            if value >=2:
                duplicates.append(key)
        
        return duplicates

