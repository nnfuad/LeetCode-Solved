# Simplify Path

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/simplify-path/

---

The problem requires converting a Unix-style absolute path into its canonical form by handling directory navigation symbols like '.' (current directory), '..' (parent directory), and collapsing multiple slashes. The solution leverages a stack-based approach to process each directory component efficiently.

**Optimal Approach:**
1. **Splitting the Path:** Split the input path by '/' to handle multiple consecutive slashes, which results in empty strings that can be filtered out.
2. **Processing Components:** Iterate through each component:
   - Skip empty strings and '.' (current directory).
   - Handle '..' by popping the last directory from the stack (if not empty).
   - Append valid directory/file names to the stack.
3. **Constructing Result:** Join the stack elements with '/' and prepend a '/' to form the canonical path.

**Time Complexity:** O(n), where n is the length of the path string, as splitting and processing each component takes linear time.
**Space Complexity:** O(n) in the worst case for storing directory names in the stack.

This approach efficiently handles all edge cases, including parent directory navigation and trailing slashes, ensuring compliance with Unix path conventions.