class Solution:
    def isHappy(self, n: int) -> bool:

        def calculate(x):
            res = 0
            while x:
                digit = x % 10
                res += digit**2
                x = x // 10
            return res

        # detect if a number has already been seen
        seen = set()

        while n != 1:
            n = calculate(n)
            if n in seen:
                return False
            seen.add(n)
            print(n)
        
        return True
