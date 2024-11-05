# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head.next or left == right:
            return head

        new_head = ListNode(0)
        new_head.next = head

        prev = new_head
        curr = head
        next = head.next
        index = 1
        while index <= right:
            if index == left:
                sublist_prev = prev
                sublist_tail = curr
            elif index > left and index < right:
                curr.next = prev
            elif index == right:
                curr.next = prev
                sublist_prev.next = curr
                sublist_tail.next = next
                break

            index += 1
            prev = curr
            curr = next
            next = next.next

        return new_head.next
