# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(NK)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        INT_MAX = 100000
        N = len(lists)
        head = ListNode(INT_MAX)
        current = head
        while True:
            min_value = INT_MAX
            next_index = -1
            for i in range(N):
                if lists[i] and lists[i].val < min_value:
                    min_value = lists[i].val
                    next_index = i

            if next_index == -1: # all lists reach None
                break

            current.next = lists[next_index]
            current = current.next
            lists[next_index] = lists[next_index].next

        return head.next

# divide and conquer, O(NlogK), K lists, N nodes
class Solution(object):
    def merge2Lists(self, list1, list2):
        head = ListNode(self.INT_MAX)
        current = head
        while list1 or list2:
            if not list1 and list2:
                current.next = list2
                current = current.next
                list2 = list2.next
            elif list1 and not list2:
                current.next = list1
                current = current.next
                list1 = list1.next
            elif list1.val < list2.val:
                current.next = list1
                current = current.next
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None

        self.INT_MAX = 100000
        while len(lists) > 1:
            N = len(lists)
            new_lists = []
            for i in range(0, N, 2):
                if i != N - 1:
                    new_lists.append(self.merge2Lists(lists[i], lists[i + 1]))
                else:
                    new_lists.append(lists[i])

            lists = new_lists

        return lists[0]
