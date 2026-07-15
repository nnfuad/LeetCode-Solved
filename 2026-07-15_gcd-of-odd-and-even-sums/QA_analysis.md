# GCD of Odd and Even Sums

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/gcd-of-odd-and-even-sums/

---

The problem requires computing the GCD of two sums: the sum of the first n odd numbers and the sum of the first n even numbers. By analyzing the formulas for these sums:

1. **Sum of first n odd numbers**: The sequence 1, 3, 5, ..., (2n-1) sums to n². This is a well-known mathematical identity.
2. **Sum of first n even numbers**: The sequence 2, 4, 6, ..., 2n sums to n(n+1). This is derived from the arithmetic series formula.

To find the GCD of these two sums:
- GCD(n², n(n+1)) = n × GCD(n, n+1). Since n and n+1 are consecutive integers, their GCD is 1. Therefore, the overall GCD simplifies to n.

This insight reduces the problem to simply returning the input value `n`, achieving O(1) time and space complexity. The solution is optimal and handles all edge cases within the given constraints.

**Key Observations**:
- Direct computation of sums is unnecessary due to the mathematical simplification.
- The GCD of consecutive integers is always 1, which is critical for the solution.
- The solution is trivial once the pattern is recognized, making it an 'Easy' problem.

**Time Complexity**: O(1) (constant time, no computations needed beyond returning the input).
**Space Complexity**: O(1) (no additional memory required).