# Remove Nth Node From End of List

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

---

The problem requires removing the nth node from the end of a singly linked list. The challenge is to do this efficiently, preferably in a single pass. The optimal approach uses two pointers to achieve O(L) time complexity, where L is the list length, and O(1) space.

**Approach:**
1. **Dummy Node:** Create a dummy node pointing to the head to handle edge cases (e.g., removing the head node).
2. **Two Pointers:** Use `first` and `second` pointers initialized at the dummy node.
3. **Advance First:** Move `first` ahead by n nodes to create a gap of n nodes between the two pointers.
4. **Traverse Together:** Move both pointers until `first` reaches the last node. At this point, `second` will be just before the node to remove.
5. **Remove Node:** Adjust `second.next` to skip the target node.

**Time Complexity:** O(L) – Single traversal of the list.
**Space Complexity:** O(1) – Only constant extra space for pointers.

**Edge Cases Handled:**
- Removing the only node in the list.
- Removing the head node when n equals the list length.
- Removing the tail node (n=1).

**Example Walkthrough:**
For `head = [1,2,3,4,5], n = 2`:
- After advancing `first` by 2 steps, it points to node 2.
- Moving both until `first` reaches node 5 (last node), `second` points to node 3.
- Removing node 4 by setting `second.next = second.next.next`.
Result: [1,2,3,5].