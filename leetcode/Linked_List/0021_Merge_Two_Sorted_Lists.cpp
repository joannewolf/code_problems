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
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		ListNode *root = new ListNode(0);
		ListNode *current = root;

		while (l1 != NULL && l2 != NULL) {
			if (l1 -> val < l2 -> val) {
				current -> next = l1;
				l1 = l1 -> next;
			}
			else {
				current -> next = l2;
				l2 = l2 -> next;
			}
			current = current -> next;
		}
		if (l1 != NULL)
			current -> next = l1;
		if (l2 != NULL)
			current -> next = l2;
				
		return root -> next;
	}
};

// by recursion
class Solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		if (l1 == NULL)
			return l2;
		else if (l2 == NULL)
			return l1;
		else if (l1 -> val < l2 -> val) {
			l1 -> next = mergeTwoLists(l1 -> next, l2);
			return l1;
		}
		else {
			l2 -> next = mergeTwoLists(l1, l2 -> next);
			return l2;
		}
	}
};