class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        d = {}
        for i in range(n):
            d[heights[i]] = names[i]
        
        heights.sort(reverse = True)

        result = []

        for h in heights:
            result.append(d[h])
        
        return result

        