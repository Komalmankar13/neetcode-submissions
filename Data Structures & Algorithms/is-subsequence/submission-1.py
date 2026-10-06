class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "" or s == t:
            return True
        
        j = 0
        for i in range(len(t)):
            if j<len(s) and t[i] == s[j]:
                j = j+1
        
        if j == len(s):
            return True
        
        else:
            return False