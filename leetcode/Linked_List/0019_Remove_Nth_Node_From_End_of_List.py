# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        N = len(nodes)
        if n == N:
            return head.next
        elif n == 1:
            nodes[-2].next = None
            return head
        else:
            nodes[N - n - 1].next = nodes[N - n + 1]
            return head
