'''
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.
'''
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:   
    # Merges two sorted lists into one sorted list, e.g.
    #   l1: 1 -> 4 -> 5     l2: 1 -> 3 -> 4     result: 1 -> 1 -> 3 -> 4 -> 4 -> 5
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)             # fake node in front of the result, so the first node attaches like the rest
        curr = dummy                    # curr is the last node of the result so far
        while l1 and l2:                # while both lists still have nodes left
            if l1.val <= l2.val:        # l1's front node is smaller (or equal)
                curr.next = l1          # attach l1's front node to the result
                l1 = l1.next            # move l1 forward past the node we just used
            else:                       # l2's front node is smaller
                curr.next = l2          # attach l2's front node to the result
                l2 = l2.next            # move l2 forward past the node we just used
            curr = curr.next            # the node we just attached is now the end of the result
        curr.next = l1 or l2            # one list ran out; attach whatever is left of the other (already sorted)
        return dummy.next               # skip the fake node, the real result starts after it

    # Merges the lists in pairs, round after round, until one list is left, e.g.
    #   round 1: [A, B, C, D, E]  ->  [AB, CD, E]
    #   round 2: [AB, CD, E]      ->  [ABCD, E]
    #   round 3: [ABCD, E]        ->  [ABCDE]
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:                   # no lists given at all
            return None

        while len(lists) > 1:           # keep going until everything is merged into one list
            merged = []                 # the lists produced by this round
            for i in range(0, len(lists), 2):   # step by 2 to take the lists in pairs: (0,1), (2,3), ...
                l1 = lists[i]           # first list of the pair
                l2 = lists[i + 1] if i + 1 < len(lists) else None  # second list, or None if the count is odd
                merged.append(self.mergeTwoLists(l1, l2))  # merge the pair (merging with None just returns l1)
            lists = merged              # this round's results are the input to the next round
        return lists[0]                 # the one list left is the fully merged answer
        

