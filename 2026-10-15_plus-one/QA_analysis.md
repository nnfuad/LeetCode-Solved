# Plus One

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/plus-one/

---

### Understanding the Problem
The problem requires us to increment a large integer represented as an array of digits by one and return the resulting array. The digits are ordered from the most significant to the least significant, and there are no leading zeros.

### Optimal Approach
To solve this problem efficiently, we can follow these steps:
1. **Iterate from the end to the beginning**: Start from the last digit and move towards the first digit.
2. **Increment the digit**: If the current digit is less than 9, simply increment it by one and return the array.
3. **Handle carry-over**: If the current digit is 9, set it to 0 and continue to the next digit to handle the carry-over.
4. **Handle the case where all digits are 9**: If all digits are 9, after setting them to 0, insert 1 at the beginning of the array.

### Time and Space Complexity
- **Time Complexity**: O(n), where n is the number of digits. In the worst case, we may need to traverse the entire array.
- **Space Complexity**: O(1) if we are modifying the input array in place. However, if we need to create a new array (for example, when all digits are 9), the space complexity becomes O(n).

### Solution Code
Below is the Python implementation based on the above approach: