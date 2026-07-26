# Merge Two Sorted Lists

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/merge-two-sorted-lists/

---

# Merge Two Sorted Lists - Analysis

## Problem Understanding
We need to merge two sorted linked lists into a single sorted linked list by splicing together the existing nodes (not creating new ones). This is a classic linked list problem that tests understanding of pointer manipulation and recursion.

## Approach Analysis

### Approach 1: Iterative with Dummy Node
- Use a dummy node to simplify edge cases
- Compare nodes from both lists and attach the smaller one
- Move pointers accordingly
- Handle remaining nodes at the end

**Time Complexity:** O(m + n) where m and n are lengths of the two lists
**Space Complexity:** O(1) - only using constant extra space

### Approach 2: Recursive
- Base case: if one list is empty, return the other
- Compare heads and recursively merge the rest
- **Time Complexity:** O(m + n)
- **Space Complexity:** O(m + n) due to call stack

## Optimal Solution
The iterative approach is preferred because:
1. O(1) space complexity vs O(m+n) for recursive
2. No risk of stack overflow for very long lists
3. More intuitive for linked list manipulation
4. Same time complexity

## Edge Cases Handled
- Empty lists (both or either)
- Lists of different lengths
- Lists with same values
- Single node lists

## Implementation Details
- Reuse existing nodes (splicing)
- Use dummy node to avoid special handling of head
- Single pass through both lists