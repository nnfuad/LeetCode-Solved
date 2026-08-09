# Climbing Stairs

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/climbing-stairs/

---

# Climbing Stairs Problem Analysis

## Problem Understanding

This is a classic dynamic programming problem where we need to find the number of distinct ways to climb a staircase with `n` steps, given that each time we can climb either 1 or 2 steps.

## Key Observations

1. **Base Cases**:
   - `n = 1`: Only 1 way (take 1 step)
   - `n = 2`: Two ways (1+1 or 2)

2. **Recurrence Relation**: For any step `n`, the number of ways to reach it equals:
   - Ways to reach step `n-1` (then take 1 step)
   - Plus ways to reach step `n-2` (then take 2 steps)
   - So: `ways(n) = ways(n-1) + ways(n-2)`

3. **Pattern Recognition**: This follows the Fibonacci sequence: 1, 2, 3, 5, 8, 13, ...

## Optimal Approach

**Algorithm**: Iterative bottom-up approach with constant space

**Why it works**: Instead of using recursion with memoization (O(n) space), we only need to keep track of the last two values to compute the current value.

## Complexity Analysis

- **Time Complexity**: O(n) - We iterate from 3 to n once
- **Space Complexity**: O(1) - We only store two variables regardless of input size

## Alternative Approaches Considered

1. **Recursive with Memoization**: O(n) time, O(n) space - Works but uses extra memory
2. **Matrix Exponentiation**: O(log n) time - Overkill for n ≤ 45, more complex implementation
3. **Golden Ratio Formula**: O(1) time - Prone to floating-point precision issues

For the given constraint (n ≤ 45), the iterative approach is optimal - simple, efficient, and exact.

## Edge Cases

- Minimum input: `n = 1` returns `1`
- Small inputs: `n = 2` returns `2`, `n = 3` returns `3`
- Maximum input: `n = 45` fits in 32-bit integer (1,134,903,170)

## Verification with Examples

- **Example 1** (n=2): ways = 2 ✓
- **Example 2** (n=3): ways = 3 ✓