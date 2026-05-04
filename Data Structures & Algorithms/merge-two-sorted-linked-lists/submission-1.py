# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create a new listnode
        # set that list node equal to another variable

        # iterate through l1 and l2
            # when a value in l1 is smaller than l2
            # set the other variable equal to l1
            # iterate the l1 list
            # else
            # set the other variable equal to l2
            # iterate the l2 list
        # iterate the other variable

        # if list1:
        #  add remaining to copy
        # elif list2
        #  add remaining to copy

        # return original listNode variable . next

        dummy = ListNode()
        copy = dummy

        while list1 and list2:
            if list1.val < list2.val:
                copy.next = list1
                list1 = list1.next
            else:
                copy.next = list2
                list2 = list2.next
            copy = copy.next
        
        if list1:
            copy.next = list1
        elif list2:
            copy.next = list2
        
        return dummy.next

