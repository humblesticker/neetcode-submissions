class Solution:
    def myPow(self, x: float, n: int) -> float:
        # edge cases
        if x == 0: return 0
        if n == 0: return 1

        # hanlde negative n
        if n < 0: 
            x = 1/x
            n = -n

        def calc(d: int):
            if d == 1: return x

            half = calc(d//2)
            if d%2 == 0: return half * half
            else: return half * half * x

        return calc(n)


"""


-3 -> 1/2, 3
n, result
3, f(1)^2 * 1/2
1, return 1/2

n = 0
x = 0
n = negative
x = negative
"""