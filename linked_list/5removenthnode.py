'''
Given the head of a linked list and an integer n, 
remove the nth node from the end of the list and return its head.
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        k = 0
        curr = head

        # find length of linked list
        while curr is not None:
            curr = curr.next
            k += 1

        # if n is greater than length
        if n > k:
            return head

        # if head node needs to be deleted
        if k - n == 0:
            head = head.next
            return head

        # reach node just before target node
        curr = head

        for i in range(1, k - n):
            curr = curr.next 

        # delete target node
        curr.next = curr.next.next

        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
n = 2
s = Solution().removeNthFromEnd(head)

