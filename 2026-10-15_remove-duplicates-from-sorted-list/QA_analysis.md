# Remove Duplicates from Sorted List

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-list/

---

The problem requires removing all duplicates from a sorted linked list such that each element appears only once. The solution must maintain the sorted order of the list.

### Approach
1. **Initial Check**: If the linked list is empty (head is None), return the list as is.
2. **Traverse the List**: Use a pointer (current) to traverse the linked list.
3. **Remove Duplicates**: For each node, check if the next node has the same value. If it does, skip the next node by pointing the current node's next to the next node's next. Repeat this until the next node has a different value or the end of the list is reached.
4. **Move Pointer**: If no duplicates are found, move the pointer to the next node.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the number of nodes in the linked list. Each node is examined exactly once.
- **Space Complexity**: O(1), as no additional space is used apart from a few pointers.

### Solution Code
```python
class Solution:
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```

### Explanation
- **Initial Check**: The loop starts with the head node. If the list is empty, the loop doesn't execute, and the head (None) is returned.
- **Traversal and Duplication Check**: The loop continues until the end of the list is reached. For each node, if the next node's value is the same as the current node's value, the next node is skipped by updating the current node's next pointer to point to the node after the next one.
- **Non-duplicate Handling**: If the next node's value is different, the current pointer moves to the next node to continue the traversal.
- **Return**: The modified linked list, now without duplicates, is returned, maintaining its sorted order.