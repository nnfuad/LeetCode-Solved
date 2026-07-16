# Add Digits

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/add-digits/

---

## Problem Analysis

**Understanding the Problem:**
Given an integer `num`, we need to repeatedly sum its digits until we get a single-digit result. This is known as finding the 'digital root' of a number.

**Examples:**
- 38 → 3+8=11 → 1+1=2
- 0 → 0

**Approach 1: Simulation (Loop)**
We can simulate the process:
1. While num >= 10, sum all digits
2. Update num to the sum
3. Return num

**Time Complexity:** O(log num) - each iteration processes log₁₀(num) digits
**Space Complexity:** O(1)

**Approach 2: Mathematical Formula (O(1) solution)**
The digital root has a beautiful mathematical property:
- If num == 0, return 0
- If num % 9 == 0, return 9
- Otherwise, return num % 9

This works because of modular arithmetic properties. The formula `(num - 1) % 9 + 1` elegantly handles all cases:
- For num=0: (0-1)%9+1 = 9, but we need to handle this edge case
- For num>0: gives the correct digital root

**Final Formula:**
```python
return 0 if num == 0 else (num - 1) % 9 + 1
```

Or equivalently: `num % 9 or 9 and num != 0` but the first form is clearer.

**Time Complexity:** O(1)
**Space Complexity:** O(1)