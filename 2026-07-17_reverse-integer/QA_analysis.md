# Reverse Integer

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/reverse-integer/

---

The problem requires reversing the digits of a 32-bit signed integer while ensuring the result remains within the 32-bit range. The key challenges are handling negative numbers, avoiding overflow during reversal, and adhering to the 32-bit integer constraints.

**Approach**:
1. **Extract Sign**: Determine if the input is positive or negative to apply the sign at the end.
2. **Process Absolute Value**: Reverse the digits of the absolute value of the input. During reversal, check for overflow at each step to ensure the intermediate result does not exceed 2^31 (the maximum absolute value allowed for any 32-bit integer).
3. **Overflow Check During Reversal**: Before updating the reversed number, verify if adding the next digit would cause it to exceed the 32-bit limit. This prevents overflow in environments that don't allow 64-bit integers.
4. **Apply Sign and Final Check**: After reversing, apply the sign and verify the result is within the 32-bit range [-2^31, 2^31 - 1]. If not, return 0.

**Time Complexity**: O(log10(n)) where n is the input value, as we process each digit. The number of digits in x is proportional to log10(x).
**Space Complexity**: O(1) since we use a constant amount of extra space.

This approach efficiently handles edge cases like maximum/minimum 32-bit values and ensures correctness without overflow by checking constraints during the reversal process.