/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// O(1) space
class Solution {
public:
	ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		ListNode *current1 = headA, *current2 = headB;
		// current1: A -> B, current2: B -> A, they will be same length and intersection will be at same number of node
		while (current1 != current2) {
			current1 = (current1 != NULL) ? current1 -> next : headB;
			current2 = (current2 != NULL) ? current2 -> next : headA;
		}
		return current1;
	}
};

// O(N) space, use set
class Solution {
public:
	ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		set<ListNode*> nodeA;
		ListNode *current = headA;
		while (current != NULL) {
			nodeA.insert(current);
			current = current -> next;
		}

		current = headB;
		while (current != NULL) {
			if (nodeA.find(current) != nodeA.end())
				return current;
			current = current -> next;
		}
		return NULL;
	}
};

// O(N) space, use vector
class Solution {
public:
	ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
		vector<ListNode*> A, B;
		ListNode *current;
		// save all nodes
		current = headA;
		while (current != NULL) {
			A.push_back(current);
			current = current -> next;
		}
		current = headB;
		while (current != NULL) {
			B.push_back(current);
			current = current -> next;
		}
		// find the intersection from tail
		if (A.size() == 0 || B.size() == 0 || A.back() != B.back())
			return NULL;
		for (int i = 0; i < min(A.size(), B.size()); i++) {
			if (A[A.size() - 1 - i] != B[B.size() - 1 - i])
				return A[A.size() - i];
		}
		return (A.size() < B.size()) ? A[0] : B[0];
	}
};