class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        
        for i in range(31):
            if(n == 2**i):
                return True
        
        return False
        