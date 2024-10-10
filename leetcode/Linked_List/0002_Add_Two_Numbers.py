# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode()
        current_node = root
        overflow = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                new_val = l2.val + overflow
                l2 = l2.next
            elif l2 is None:
                new_val = l1.val + overflow
                l1 = l1.next
            else:
                new_val = l1.val + l2.val + overflow
                l1 = l1.next
                l2 = l2.next

            if new_val > 9:
                overflow = new_val // 10
                new_val %= 10
            else:
                overflow = 0
            current_node.next = ListNode(new_val)
            current_node = current_node.next

        if overflow != 0:
            current_node.next = ListNode(overflow)

        return root.next
