# Longest Valid Parentheses

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/longest-valid-parentheses/

---

# Longest Valid Parentheses - Analysis

## Problem Understanding
Given a string of parentheses, find the length of the longest contiguous substring that forms valid (well-formed) parentheses.

## Key Insights
1. Valid parentheses must have matching opening '(' with closing ')' in correct order
2. We need to find the **longest contiguous** valid substring, not total count
3. Invalid parentheses can break valid sequences

## Optimal Approaches

### Approach 1: Stack-based (Recommended)
**Idea**: Use a stack to track indices of unmatched opening parentheses. Initialize with -1 as base marker.

**Algorithm**:
- Push -1 onto stack initially
- For '(' at index i: push i
- For ')' at index i: pop from stack
  - If stack empty: push current index as new base
  - If stack not empty: current valid length = i - stack.top
- Track maximum length

**Complexity**: O(n) time, O(n) space

### Approach 2: Dynamic Programming
**Idea**: dp[i] = length of longest valid parentheses ending at i

**Recurrence**:
- If s[i] == '(' : dp[i] = 0
- If s[i] == ')' and s[i-1] == '(' : dp[i] = dp[i-2] + 2
- If s[i] == ')' and s[i-1] == ')' : check if s[i - dp[i-1] - 1] == '(' then dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]

**Complexity**: O(n) time, O(n) space

### Approach 3: Two-pass Scanning
**Idea**: Scan left-to-right and right-to-left, tracking counts

**Complexity**: O(n) time, O(1) space

## Why Stack-based is Chosen
- Intuitive and easier to understand
- Handles nested cases correctly
- Single pass solution
- Natural handling of validation

## Edge Cases Handled
- Empty string: returns 0
- All unmatched: returns 0
- Single valid pair: returns 2
- Nested valid patterns: handled correctly
- Multiple separate valid groups: takes maximum