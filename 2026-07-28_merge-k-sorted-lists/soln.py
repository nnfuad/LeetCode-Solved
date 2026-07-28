import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists into one sorted linked list.
        
        Args:
            lists: Array of k linked lists, each sorted in ascending order
        
        Returns:
            Merged sorted linked list
        """
        if not lists:
            return None
        
        # Create min-heap to store (value, index, node) tuples
        # Index is used as tiebreaker to avoid comparing ListNode objects
        heap = []
        
        # Initialize heap with the head of each non-empty list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Dummy node to build the result list
        dummy = ListNode(0)
        current = dummy
        
        # Process until heap is empty
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # If this node has a next node, add it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next