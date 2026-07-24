# String to Integer (atoi)

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/string-to-integer-atoi/

---

# String to Integer (atoi) Problem Analysis

## Problem Understanding
We need to implement the `myAtoi` function that converts a string to a 32-bit signed integer following specific rules:

1. **Whitespace Handling**: Ignore leading whitespace characters
2. **Sign Detection**: Check for optional '+' or '-' prefix
3. **Digit Extraction**: Read consecutive digits until a non-digit character
4. **Overflow Protection**: Clamp result to 32-bit signed integer range [-2³¹, 2³¹-1]

## Key Insights
- The function must handle edge cases: empty strings, strings with no digits, overflow conditions
- We need to process characters sequentially with proper bounds checking
- The 32-bit signed integer range is: MIN = -2147483648, MAX = 2147483647

## Approach
The optimal approach is a single-pass linear scan:

1. Skip leading whitespace characters
2. Detect optional sign character ('-' or '+')
3. Extract consecutive digit characters
4. Convert to integer and apply sign
5. Clamp to 32-bit range if necessary

## Complexity Analysis
- **Time Complexity**: O(n) where n is the length of the string - we make a single pass through the string
- **Space Complexity**: O(1) - we only use a constant amount of extra space

## Edge Cases to Consider
- Empty string or whitespace-only string → return 0
- String starting with non-digit characters → return 0
- Large numbers causing overflow → clamp to MIN or MAX
- Leading zeros in the number part → handled naturally by integer conversion
- Multiple signs or signs in wrong positions → only first valid sign matters

## Solution Implementation