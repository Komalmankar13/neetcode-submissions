class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 Pointer Method

        left = 0
        right= len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
            
            elif not s[right].isalnum():
                right -= 1
            
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            
            else:
                return False
        return True

        # result = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         result += s[i].lower()
        
        # reverse = result[::-1]

        # if reverse == result:
        #     return True
        
        # else:
        #     return False
        