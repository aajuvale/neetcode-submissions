# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hashSet = set()

        while head.next:
            if head.next.val in hashSet:
                return True
            hashSet.add(head.val)
            head = head.next
        return False
        