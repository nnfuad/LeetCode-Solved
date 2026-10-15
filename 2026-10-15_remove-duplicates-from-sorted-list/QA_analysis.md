# Remove Duplicates from Sorted List

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/

---

### Problem Analysis

The problem requires us to remove duplicate nodes from a sorted linked list such that each element appears only once. The list remains sorted after the removal. Given that the list is already sorted, duplicates will be consecutive, simplifying the problem.

### Optimal Approach

The optimal approach involves traversing the linked list while comparing each node's value with the next node's value. If they are the same, we skip the next node by adjusting the `next` pointer of the current node to point to the node after the next one. This effectively removes the duplicate node. The traversal continues until the end of the list is reached.

#### Time and Space Complexity

- **Time Complexity**: O(n), where n is the number of nodes in the linked list. This is because each node is checked exactly once.
- **Space Complexity**: O(1), as no additional space is used apart from a few pointers for traversal.

### Solution Code

The solution involves traversing the linked list and removing duplicates by adjusting the `next` pointers of the nodes.