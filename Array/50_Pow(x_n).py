class Solution: 
    def pow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return x * self.pow(x * x, n // 2) if n % 2 else self.pow(x * x, n // 2)