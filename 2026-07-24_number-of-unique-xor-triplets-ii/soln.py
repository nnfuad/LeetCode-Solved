from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniq = list(set(nums))
        two_bits = 0
        for a in uniq:
            for b in uniq:
                two_bits |= 1 << (a ^ b)
        three_bits = 0
        t_bits = two_bits
        while t_bits:
            lsb = t_bits & -t_bits
            t = lsb.bit_length() - 1
            t_bits ^= lsb
            for c in uniq:
                three_bits |= 1 << (t ^ c)
        return three_bits.bit_count()