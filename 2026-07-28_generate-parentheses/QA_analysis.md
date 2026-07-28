# Generate Parentheses

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/generate-parentheses/

---

The problem requires generating all valid combinations of parentheses given n pairs. A valid combination means every opening parenthesis has a corresponding closing one and they are properly nested.

**Approach:**
This is a classic backtracking problem. We build strings incrementally, ensuring at each step that we only add valid characters. Specifically:
1. We can add an opening parenthesis '(' if we haven't used all n of them.
2. We can add a closing parenthesis ')' only if there are more opening than closing parentheses used so far.

**Algorithm:**
- Use a recursive backtracking function that tracks the current string, count of open parentheses, and count of close parentheses.
- When the string's length reaches 2n, it's a valid combination and added to the result.
- Prune invalid paths early by only allowing valid moves.

**Complexity Analysis:**
- **Time Complexity:** O(4^n / √n), which is the nth Catalan number. This represents the number of valid parentheses combinations.
- **Space Complexity:** O(n) for the recursion stack depth (maximum depth is 2n), plus O(4^n / √n) for storing all valid combinations.

**Optimization:**
Using a list to build the current string (instead of string concatenation) improves efficiency, as list append/pop operations are O(1).