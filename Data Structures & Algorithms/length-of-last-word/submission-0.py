class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        conversion = s.split()
        lastWorld = conversion[-1]
        count = 0
        for i in range(len(lastWorld)):
            count = count + 1
        
        return count
        