# Remove Element

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/remove-element/

---

The problem requires removing all instances of a given value 'val' from an array in-place and returning the count of remaining elements. The key challenge is to perform this operation efficiently without using extra space.

**Optimal Approach:**
Using a two-pointer technique is the most efficient way. One pointer (let's call it 'k') tracks the position where the next valid element (not equal to 'val') should be placed. The other pointer traverses the array. For each element, if it is not equal to 'val', we place it at the position indicated by 'k' and increment 'k'. This ensures all valid elements are moved to the front of the array in O(n) time with O(1) additional space.

**Time Complexity:** O(n) where n is the length of the array. Each element is processed exactly once.
**Space Complexity:** O(1) as the operation is performed in-place without additional data structures.

**Example Walkthrough:**
For input [3,2,2,3] and val = 3:
- Iterate through the array. The first 3 is skipped. The next element 2 is placed at index 0, k becomes 1. The next 2 is placed at index 1, k becomes 2. The last 3 is skipped. The result is k=2 with the first two elements [2,2].

This approach handles all edge cases, including empty arrays and arrays with all elements equal to 'val'.