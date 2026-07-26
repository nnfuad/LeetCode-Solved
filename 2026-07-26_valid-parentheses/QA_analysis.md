# Valid Parentheses

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/valid-parentheses/

---

## Problem Analysis

### Understanding the Problem
We need to validate a string containing only parentheses characters '()', '[]', '{}'. A string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order (LIFO - Last In, First Out)
3. Every close bracket has a corresponding open bracket of the same type

### Key Insights
- This is a classic **stack-based problem**
- The order matters: brackets must close in reverse order of opening (nested structure)
- Example: "([)]" is INVALID because ')' would need to close '(' before ']' closes '['
- Example: "([])" is VALID because structure is properly nested

### Optimal Approach: Stack
The stack data structure is perfect here because:
- Last opened bracket must be first closed (LIFO property)
- We can push opening brackets and pop when we encounter closing brackets
- At the end, stack should be empty for a valid string

### Algorithm Steps
1. Initialize an empty stack
2. Create a mapping from closing brackets to their corresponding opening brackets
3. Iterate through each character:
   - If it's a closing bracket: check if stack is non-empty and top matches
   - If it's an opening bracket: push to stack
4. Return true if stack is empty, false otherwise

### Time and Space Complexity
- **Time Complexity: O(n)** - Single pass through the string
- **Space Complexity: O(n)** - In worst case (all opening brackets), stack stores n elements

### Edge Cases
- Single character: "(" → false, ")" → false
- All opening: "(((" → false
- All closing: "))) " → false
- Empty stack with closing: "]" → false (handled by checking stack non-empty)

### Implementation Note
Using a hash map for bracket mapping makes the code cleaner and more maintainable than multiple if-else conditions.