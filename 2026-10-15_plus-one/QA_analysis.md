# Plus One

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/plus-one/

---

### Problem Analysis

The task is to increment a large integer represented as an array of digits by one. The digits are arranged from the most significant digit (leftmost) to the least significant digit (rightmost). The problem requires handling cases like when the last digit is a 9, which would cause a carry-over effect.

### Approach

1. **Start from the Last Digit**: Begin processing from the least significant digit (the last element in the array).
2. **Increment and Check for Carry**: Increment the digit by one. If the result is less than 10, simply update the digit and return the array.
3. **Handle Carry**: If the result is 10, set the digit to 0 and propagate the carry to the next left digit.
4. **Edge Case**: If all digits propagate carry and leave a carry of 1 (e.g., `[9, 9, 9]`), insert a new digit `1` at the beginning of the array.

### Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of the array. In the worst case, we iterate through the entire array.
- **Space Complexity**: O(1), except for the space required for the output. We modify the input array in place and only allocate additional space if a new digit needs to be added.

### Solution Implementation

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
```

### Explanation of the Solution

1. **Iterate through the array from the end**: The `for` loop ensures we process digits from right to left.
2. **Check if the digit is less than 9**: If so, increment the digit and return the updated array. No need for further processing.
3. **Set the digit to 0 if it’s 9**: Continue to propagate the carry to the next digit.
4. **Handle the case where all digits were 9**: After the loop, if all digits were 9, prepend a `1` to the array.

This solution ensures efficiency and handles edge cases effectively.