# Merge k Sorted Lists

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/merge-k-sorted-lists/

---

## Problem Analysis

We need to merge k sorted linked lists into a single sorted linked list. Each individual list is already sorted in ascending order.

### Key Observations:
1. We have k separate sorted linked lists
2. We need to merge them efficiently into one sorted list
3. The total number of nodes across all lists is bounded by 10^4

### Approach Selection:

**Option 1: Min-Heap (Priority Queue)**
- Maintain a min-heap of the current head nodes from all lists
- Always extract the minimum and add the next node from that list to the heap
- Time: O(N log k), Space: O(k) where N = total nodes, k = number of lists

**Option 2: Divide and Conquer**
- Merge lists pairwise: merge(0,1), merge(2,3), etc.
- Recursively merge the results
- Time: O(N log k), Space: O(log k) for recursion stack

**Option 3: Brute Force**
- Collect all nodes, sort, create new list
- Time: O(N log N), Space: O(N)

### Optimal Solution: Min-Heap Approach
The min-heap approach is optimal because:
- Direct and intuitive implementation
- O(N log k) time complexity is optimal (we must examine each node)
- O(k) space for the heap
- Avoids recursion stack overhead

### Implementation Details:
- Use a dummy node to build the result list
- Push (value, index, node) tuples to handle equal values (index as tiebreaker)
- Always pop minimum, attach to result, push next node from same list

### Edge Cases:
- Empty input array (k=0)
- All lists empty
- Single list
- Lists with equal values