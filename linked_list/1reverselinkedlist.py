'''
Given the beginning of a singly linked list head, 
reverse the list, and return the new beginning of the list.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        # loop through linked list
        while curr is not None:
            nextNode = curr.next # 1. save the rest of the list
            curr.next = prev     # 2. flip arrow to point backwards
            prev = curr          # 3. move prev forward
            curr = nextNode      # 4. move curr forward
            

def printList(node: ListNode):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(values)


head = ListNode(0, ListNode(1, ListNode(3, ListNode(4))))
s = Solution().reverseList(head)
