/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
	ListNode* reverseBetween(ListNode* head, int m, int n) {
		if (head == NULL || head -> next == NULL || m == n)
			return head;

		ListNode zero(0);
		ListNode *newhead = &zero, *sublistPrevious, *sublistTail;
		ListNode *previous = newhead, *current = head, *next = head -> next;
		int count = 1;

		newhead -> next = head;
		while (true) {
			if (count == m) {
				sublistPrevious = previous;
				sublistTail = current;
			}
			else if (count > m && count < n) {
				current -> next = previous;
			}
			else if (count == n) {
				current -> next = previous;
				sublistPrevious -> next = current;
				sublistTail -> next = next;
				break;
			}
			count ++;
			previous = current;
			current = next;
			next = next -> next;
		}
		return (newhead -> next);
	}
};

class Solution {
public:
	ListNode* reverseBetween(ListNode* head, int m, int n) {
		if (head == NULL || head -> next == NULL || m == n)
			return head;

		ListNode *newHead = new ListNode(0);
		ListNode *sublistPrevious = newHead, *sublistStart, *then;

		newHead -> next = head;
		for (int i = 1; i < m; i++)
			sublistPrevious = sublistPrevious -> next;
		sublistStart = sublistPrevious -> next;
		then = sublistStart -> next;

		for (int i = 0; i < n - m; i++) {
			sublistStart -> next = then -> next;
			then -> next = sublistPrevious -> next;
			sublistPrevious -> next = then;
			then = sublistStart -> next;
		}

		return (newHead -> next);
	}
};