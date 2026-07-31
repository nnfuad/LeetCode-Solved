class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        
        while curr:
            # Check if there are at least k nodes remaining
            temp = curr
            count = 0
            while temp and count < k:
                temp = temp.next
                count += 1
            if count < k:
                break
            
            # Reverse the next k nodes
            original_curr = curr
            prev_rev = None
            next_node = None
            for _ in range(k):
                next_node = curr.next
                curr.next = prev_rev
                prev_rev = curr
                curr = next_node
            
            # Connect the previous part to the new head
            prev.next = prev_rev
            # Connect the tail of the reversed group to the next part
            original_curr.next = curr
            # Update prev to the tail of the reversed group
            prev = original_curr
        
        return dummy.next