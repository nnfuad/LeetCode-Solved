# Swap Nodes in Pairs

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/swap-nodes-in-pairs/

---

The problem requires swapping every two adjacent nodes in a linked list without modifying node values. The key is to adjust pointers appropriately.

**Optimal Approach**: A recursive solution is elegant and straightforward. The base case handles empty or single-node lists. For each pair, swap the first two nodes and recursively process the remaining list. This approach leverages the call stack for traversal, making the code concise.

**Time and Space Complexity**:
- Time: O(n) where n is the number of nodes, as each node is processed once.
- Space: O(n) due to recursion depth (up to n/2 levels).

**Alternative Approach**: An iterative method using a dummy node and pointer manipulation achieves O(1) space but requires more code. The recursive solution is preferred for its simplicity here.