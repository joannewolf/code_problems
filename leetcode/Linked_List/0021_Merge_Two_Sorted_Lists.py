# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        root = ListNode() # temp root
        current_node = root
        while list1 is not None or list2 is not None:
            if list1 is None:
                current_node.next = list2
                list2 = list2.next
            elif list2 is None:
                current_node.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next

            current_node = current_node.next

        return root.next
