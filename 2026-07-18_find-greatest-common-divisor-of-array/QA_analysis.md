# Find Greatest Common Divisor of Array

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/find-greatest-common-divisor-of-array/

---

## Problem Analysis
The problem requires finding the greatest common divisor (GCD) of the smallest and largest elements in an integer array. The solution involves two main steps: identifying the minimum and maximum values in the array, then computing their GCD.

## Optimal Approach
1. **Find Minimum and Maximum**: Traverse the array to find the smallest and largest elements. This can be done in O(n) time using built-in functions or a single pass.
2. **Compute GCD**: Use the Euclidean algorithm or Python's `math.gcd` function to compute the GCD of the two values. The Euclidean algorithm is efficient with O(log(min(a, b))) time complexity.

## Time and Space Complexity
- **Time Complexity**: O(n) for finding min/max + O(log(min)) for GCD. Overall O(n).
- **Space Complexity**: O(1) as only a few variables are used.

## Edge Cases Handled
- Arrays with identical elements (e.g., [3,3]).
- Arrays where one element is a multiple of the other (e.g., [4,8]).
- Minimum and maximum values being 1 (e.g., [1, 1000]).

## Implementation
The solution uses Python's `min()`, `max()`, and `math.gcd()` functions for clarity and efficiency.