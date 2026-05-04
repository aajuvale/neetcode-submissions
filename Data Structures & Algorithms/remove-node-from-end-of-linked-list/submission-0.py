# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # remove the nth node from the end of the list and return the beginning
        # 1, 4, 5, 6 and n = 2, output = 1 4 6
        dummyNode = ListNode(0, head)
        left = dummyNode
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummyNode.next

        