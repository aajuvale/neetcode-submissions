class Solution:
    def myPow(self, x: float, n: int) -> float:

        res = 1.000
        # if n > 0:
        for i in range(abs(n)):
            print(i)
            print(x)
            print(res)
            res *= x
        if n < 0:
            return 1/res
        elif n == 0:
            return 1

        return res