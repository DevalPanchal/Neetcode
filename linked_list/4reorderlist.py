'''
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:

[0, n-1, 1, n-2, 2, n-3, ...]

These numbers represent node positions, not the values stored in the nodes.

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # store every node in list
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        i = 0
        j = len(nodes) - 1


        while i < j:
            nodes[i].next = nodes[j] # front points to back
            i += 1 # increase to next node
            if i == j:
                break
            nodes[j].next = nodes[i] # back points to the next front
            j -= 1

        nodes[i].next = None # last node must end the list
        
        

head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
s = Solution().reorderList(head)
