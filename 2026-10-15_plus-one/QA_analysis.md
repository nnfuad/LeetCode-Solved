# Plus One

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/plus-one/

---

### Problem Analysis

The problem requires us to increment a large integer represented as an array of digits by one and return the resulting array of digits. The digits are ordered from most significant to least significant, and there are no leading zeros.

### Optimal Approach

1. **Iterate from the end**: Start from the last digit of the array and move towards the beginning.
2. **Increment and carry**: Increment the current digit by one. If the digit becomes 10, set it to 0 and continue to the next digit (carry over).
3. **Handle leading carry**: If all digits are processed and there's still a carry (e.g., `[9, 9]` becomes `[1, 0, 0]`), insert a `1` at the beginning of the array.
4. **Return the result**: Return the modified array of digits.

### Time and Space Complexity

- **Time Complexity**: O(n), where `n` is the number of digits. In the worst case, we traverse the entire array once.
- **Space Complexity**: O(1), as we are modifying the input array in place and not using any additional space.

### Solution

The solution involves iterating through the array from the end, incrementing the digit, and handling the carry. If a carry is still present after processing all digits, we insert a `1` at the beginning of the array.