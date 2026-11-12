class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result += s[i].lower()
        
        reverse = result[::-1]

        if reverse == result:
            return True
        
        else:
            return False
        