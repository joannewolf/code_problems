/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// by iteration
class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		if (head == NULL || head -> next == NULL)
			return head;
		ListNode *previous = NULL, *current = head;
		while (current != NULL) {
			ListNode *nextTemp = current -> next;
			current -> next = previous;
			previous = current;
			current = nextTemp;
		}

		return previous;
	}
};

// by recursion
class Solution {
public:
	ListNode* reverseList(ListNode* head) {
		if (head == NULL || head -> next == NULL)
			return head;

		ListNode *newHead = reverseList(head -> next);
		head -> next -> next = head;
		// ListNode *current = newHead;
		// while (current -> next != NULL) {
		// 	current = current -> next;
		// }
		// current -> next = head;
		head -> next = NULL;

		return newHead;
	}
};