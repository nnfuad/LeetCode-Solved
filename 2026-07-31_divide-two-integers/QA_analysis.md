# Divide Two Integers

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/divide-two-integers/

---

The problem requires dividing two integers without using multiplication, division, or mod operators, and truncating the result toward zero. The solution must handle 32-bit signed integer overflow correctly.

### Approach
1. **Sign Determination**: Calculate the sign of the result by checking if the dividend and divisor have different signs.
2. **Absolute Values**: Work with the absolute values of the dividend and divisor to simplify calculations.
3. **Bitwise Division**: Use bit shifting to efficiently subtract multiples of the divisor from the dividend:
   - For each iteration, find the maximum power of two (via bit shifts) such that `divisor * 2^shift` is less than or equal to the current dividend.
   - Subtract this value from the dividend and add `2^shift` to the quotient.
4. **Clamping**: Ensure the result stays within the 32-bit signed integer range.

### Complexity
- **Time Complexity**: O(log N), where N is the dividend. Each iteration reduces the dividend significantly using bit shifts.
- **Space Complexity**: O(1), as no additional data structures are used.

### Edge Cases Handled
- Division by -1 when the dividend is the minimum 32-bit integer.
- Division resulting in values exceeding 32-bit integer limits.
- Truncation toward zero for positive and negative results.

### Code Implementation
The solution uses bit manipulation to efficiently compute the quotient through repeated subtraction of exponentially scaled divisors, then clamps the result to the 32-bit integer range.