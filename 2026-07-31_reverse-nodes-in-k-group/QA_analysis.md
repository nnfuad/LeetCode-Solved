# Reverse Nodes in k-Group

**Difficulty:** Hard

**Link:** https://leetcode.com/problems/reverse-nodes-in-k-group/

---

The problem requires reversing a linked list in groups of k nodes. The key challenge is to reverse each group while maintaining the connections between the groups and handling the case when the remaining nodes are fewer than k. 

**Optimal Approach:**
An iterative approach is used with a dummy node to simplify edge cases. The algorithm proceeds as follows:
1. **Initialization:** Create a dummy node pointing to the head to handle the head changes easily. Use pointers `prev` (tracks the end of the previous reversed group) and `curr` (current node being processed).
2. **Check Group Size:** For each group starting at `curr`, traverse k nodes to ensure there are enough nodes to reverse. If not, break.
3. **Reverse the Group:** Reverse the next k nodes using a standard reversal technique, keeping track of the new head (`prev_rev`) and the original head (which becomes the tail).
4. **Reconnect:** Link the previous group's end (`prev`) to the new head (`prev_rev`), and set the tail's next to the next group's start (`curr`). Move `prev` to the tail and `curr` to the next group's start.
5. **Repeat:** Continue until all groups are processed.

**Time Complexity:** O(n), where n is the number of nodes. Each node is visited a constant number of times.
**Space Complexity:** O(1), as we use only a fixed number of pointers, satisfying the follow-up requirement.

This approach efficiently handles all edge cases, including when the remaining nodes are fewer than k, ensuring they remain in their original order.