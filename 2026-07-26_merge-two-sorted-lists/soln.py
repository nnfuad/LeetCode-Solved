class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the merged list's head
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and merge them in sorted order
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes from either list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next