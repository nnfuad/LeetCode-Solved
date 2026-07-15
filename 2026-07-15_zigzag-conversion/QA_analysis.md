# Zigzag Conversion

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/zigzag-conversion/

---

# Zigzag Conversion Problem Analysis

## Problem Understanding
The task is to convert a string into a zigzag pattern across a given number of rows, then read the characters line by line. For example, "PAYPALISHIRING" with 3 rows forms:

```
P   A   H   N
A P L S I I G
Y   I   R
```

Reading row by row gives "PAHNAPLSIIGYIR".

## Key Observations
1. **Pattern Cycle**: The zigzag pattern repeats every `2 * numRows - 2` characters (called cycle length).
   - For numRows=3: cycle = 4
   - For numRows=4: cycle = 6

2. **Row Assignment**: Characters follow a predictable row pattern:
   - Goes down: rows 0 → 1 → 2 → ... → numRows-1
   - Goes up: rows numRows-2 → numRows-3 → ... → 1 → 0
   - Repeats

3. **Edge Cases**: When numRows=1, the string remains unchanged.

## Optimal Approach
### Direct Simulation (Recommended)
Track current row and direction as we iterate through the string:
- Start at row 0, direction = +1 (going down)
- When reaching row numRows-1, reverse direction to -1
- When reaching row 0, reverse direction to +1
- Append each character to its respective row

**Time Complexity**: O(n) where n is string length - single pass through the string.
**Space Complexity**: O(n) for storing characters in rows before concatenation.

### Mathematical Index Pattern (Alternative)
For each row i, characters appear at positions:
- Row 0 and numRows-1: i, i+cycle, i+2*cycle, ...
- Middle rows: i, cycle-i, i+cycle, cycle-i+cycle, ...

This approach computes indices directly without simulation.

## Solution Implementation
I'll use the direct simulation approach as it's intuitive, handles all edge cases naturally, and achieves optimal O(n) time complexity.