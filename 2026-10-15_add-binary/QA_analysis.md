# Add Binary

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/add-binary/

---

### Problem Analysis

Given two binary strings `a` and `b`, the goal is to compute their sum and return the result as a binary string. Binary addition follows the same rules as decimal addition but is simpler, involving only four possible cases for each digit addition:

1. 0 + 0 = 0
2. 0 + 1 = 1
3. 1 + 0 = 1
4. 1 + 1 = 10 (which means 0 with a carry of 1)

### Approach

1. **Initialize Pointers and Carry**: Start from the end of both strings and move towards the beginning. Keep track of the carry.
2. **Iterate and Add Digits**: For each iteration, take the current digits of `a` and `b` (if they exist), convert them to integers, sum them along with the carry.
3. **Compute Current Bit and Carry**: The current bit in the result is `sum % 2`, and the new carry is `sum // 2`.
4. **Handle Remaining Carry**: After processing all digits, if there's any remaining carry, prepend it to the result.
5. **Return Result**: The result is constructed by prepending each computed bit during iteration.

### Time Complexity

- **O(n)**: where n is the maximum length between the two strings. We process each digit of the strings once.

### Space Complexity

- **O(n)**: The space required to store the result, which can be at most n + 1 bits long.

### Solution Code

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            total = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
        
        return ''.join(reversed(result))
```

### Explanation

1. **Initialization**: We start with `carry` set to 0 and empty `result` list. Pointers `i` and `j` are initialized to the last index of strings `a` and `b` respectively.
2. **Loop Until All Digits and Carry are Processed**: The loop runs as long as there are digits left in either string or there is a carry to process.
3. **Digit Extraction**: For each iteration, extract the current digit from `a` and `b` (or 0 if the pointer is out of bounds).
4. **Sum and Carry Calculation**: Sum the digits along with the carry. The current bit is `total % 2`, and the new carry is `total // 2`.
5. **Append Result**: Append the computed bit to the result list and decrement the pointers.
6. **Reverse and Return**: Since we processed digits from least significant to most significant, reverse the result list to get the correct order before joining into a string.