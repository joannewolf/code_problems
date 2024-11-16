# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        odd_head, even_head = ListNode(0), ListNode(0)
        odd_tail, even_tail = odd_head, even_head
        flag = 1
        current = head
        while current:
            if flag == 1:
                odd_tail.next = current
                odd_tail = odd_tail.next
                flag = 2
            elif flag == 2:
                even_tail.next = current
                even_tail = even_tail.next
                flag = 1

            current = current.next

        odd_tail.next = even_head.next
        even_tail.next = None
        return odd_head.next
