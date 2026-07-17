import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        d = math.gcd(p, q)
        m = p // d
        n = q // d
        if m % 2 == 0 and n % 2 == 1:
            return 2
        elif m % 2 == 1 and n % 2 == 0:
            return 0
        else:
            return 1