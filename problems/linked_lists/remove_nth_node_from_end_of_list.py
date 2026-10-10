"""19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Approach: 
Time complexity: O(n)
Space complexity: O(1)
Edge cases: n = length of linked list
Lessons / mistakes:
"""

from __future__ import annotations

from problems.structures import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        i = length - n
        dummy = head
        if i == 0
            dummy = dummy.next
            return dummy
        while i > 1:
            dummy = dummy.next
            i -= 1
        if dummy.next:
            dummy.next = dummy.next.next
        else: dummy.next = None
        return head


