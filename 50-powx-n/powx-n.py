class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1

        # Handle negative power
        if n < 0:
            return 1 / self.myPow(x, -n)

        # If n is even
        if n % 2 == 0:
            half = self.myPow(x, n // 2)
            return half * half
        # If n is odd
        else:
            return x * self.myPow(x, n - 1)
        
    

        