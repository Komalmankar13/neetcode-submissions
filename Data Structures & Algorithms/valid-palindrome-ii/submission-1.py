class Solution:
    def validPalindrome(self, s: str) -> bool:
        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result += s[i].lower()
        
        reverse = result[::-1]
        if reverse == result:
            return True

        for i in range(len(result)):
            temp = result[:i] + result[i+1:]
            reverse = temp[::-1]

            if temp == reverse:
                return True
            
        return False
        