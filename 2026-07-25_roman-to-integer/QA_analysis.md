# Roman to Integer

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/roman-to-integer/

---

# Roman to Integer Problem Analysis

## Problem Overview
Convert a Roman numeral string to its corresponding integer value. Roman numerals use seven symbols (I, V, X, L, C, D, M) with specific values. The key challenge is handling subtractive combinations where a smaller numeral precedes a larger one (e.g., IV = 4, IX = 9).

## Key Insights
1. **Symbol Values**:
   - I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
2. **Subtractive Cases**:
   - I can precede V (4) and X (9)
   - X can precede L (40) and C (90)
   - C can precede D (400) and M (900)
3. **Algorithm Strategy**:
   - Process the string from right to left
   - Compare current symbol's value with the previous (right-side) value
   - If current < previous: subtract current from total
   - Else: add current to total

## Optimal Approach
**Time Complexity**: O(n) - Single pass through the string
**Space Complexity**: O(1) - Fixed-size hash map for symbol values

## Algorithm Steps
1. Create a hash map for Roman symbol to integer conversion
2. Initialize total and previous value trackers
3. Iterate through the string in reverse order
4. For each symbol:
   - Get its integer value
   - If current < previous: subtract from total
   - Else: add to total
   - Update previous value
5. Return the accumulated total

## Example Walkthrough
For "MCMXCIV":
- Reversed: "VICMXCM"
- Processing:
  - V(5) → add → total=5
  - I(1) < 5 → subtract → total=4
  - C(100) > 1 → add → total=104
  - X(10) < 100 → subtract → total=94
  - M(1000) > 10 → add → total=1094
  - C(100) < 1000 → subtract → total=994
  - M(1000) > 100 → add → total=1994