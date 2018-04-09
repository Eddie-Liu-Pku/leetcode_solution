# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #快慢指针
        fast=slow=head
        while fast and fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return Falses