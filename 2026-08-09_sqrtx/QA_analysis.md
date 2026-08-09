# Sqrt(x)

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/sqrtx/

---

# Sqrt(x) - Problem Analysis

## Problem Understanding
We need to compute the integer square root of a non-negative integer `x`, rounded down to the nearest integer. The constraint is that we cannot use built-in exponent functions like `pow(x, 0.5)` or `x ** 0.5`.

## Examples
- `x = 4` → Output: `2` (since √4 = 2)
- `x = 8` → Output: `2` (since √8 ≈ 2.828, rounded down to 2)

## Constraints
- `0 <= x <= 2^31 - 1`
- No built-in exponent functions allowed

## Approaches Analysis

### 1. Linear Search (Brute Force)
Iterate from 1 to x, finding the largest i where i² ≤ x.
- **Time Complexity**: O(√x)
- **Space Complexity**: O(1)

### 2. Binary Search (Optimal)
Use binary search to find the largest integer whose square is ≤ x.
- **Time Complexity**: O(log x)
- **Space Complexity**: O(1)

### 3. Newton's Method
Newton's method iteratively improves the guess: guess = (guess + x/guess) / 2
- **Time Complexity**: O(log log x) approximately
- **Space Complexity**: O(1)

## Optimal Approach: Binary Search
Binary search is chosen because:
1. It efficiently narrows down the search space in O(log x) time
2. Handles edge cases well (x = 0, x = 1)
3. Works within the 32-bit integer constraint
4. No floating-point operations needed

## Algorithm Steps
1. Handle edge cases: if x < 2, return x directly
2. Set search bounds: left = 1, right = x/2
3. Binary search: find the largest mid where mid² ≤ x
4. Return the result after search completes

## Edge Cases
- `x = 0`: return 0
- `x = 1`: return 1
- `x = 2`: return 1
- Maximum value `2^31 - 1`: needs proper integer handling