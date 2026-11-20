'''
You are given two non-empty linked lists, l1 and l2, 
where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 321 
is represented as 1 -> 2 -> 3 -> in the linked list.

Each of the nodes contains a single digit. You may assume the 
two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            # pointer for l1 and l2
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # start adding all possible values
            sum = carry + x + y

            # get remainder
            carry = sum // 10

            # create new listNode for next node
            current.next = ListNode(sum % 10)

            # move node
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next



l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(4, ListNode(9, ListNode(6)))

s = Solution().addTwoNumbers(l1, l2)
