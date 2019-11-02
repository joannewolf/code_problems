/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// O(3N), reverse, plus one, then reverse back
class Solution {
public:
	ListNode* plusOne(ListNode* head) {
		// reverse the linked list
		ListNode *previous = NULL, *current = head;
		while (current != NULL) {
			ListNode *nextTemp = current -> next;
			current -> next = previous;
			previous = current;
			current = nextTemp;
		}
		
		// plus one
		ListNode *tail = previous;
		current = previous;
		int temp = previous -> val + 1;
		int carry = temp / 10;
		current -> val = temp % 10;
		current = current -> next;
		while (carry != 0 && current != NULL) {
			temp = current -> val + carry;
			carry = temp / 10;
			current -> val = temp % 10;
			previous = previous -> next;
			current = current -> next;
		}
		if (carry != 0) {
			ListNode *newNode = new ListNode(carry);
			previous -> next = newNode;
			previous = previous -> next;
		}

		// reverse back the linked list
		previous = NULL;
		current = tail;
		while (current != NULL) {
			ListNode *nextTemp = current -> next;
			current -> next = previous;
			previous = current;
			current = nextTemp;
		}
		
		return previous;
	}
};

// O(2N), use pointer
class Solution {
public:
	ListNode* plusOne(ListNode* head) {
		ListNode *propogationEnd = NULL, *current = head;

		// find the end of propogation
		while (current != NULL) {
			if (current -> val != 9)
				propogationEnd = current;
			current = current -> next;
		}

		// every node after the end of propogation should add 1
		if (propogationEnd == NULL) {
			propogationEnd = new ListNode(0);
			propogationEnd -> next = head;
			head = propogationEnd;
		}
		while (propogationEnd != NULL) {
			propogationEnd -> val = (propogationEnd -> val + 1) % 10;
			propogationEnd = propogationEnd -> next;
		}
		return head;
	}
};

// O(N) space
class Solution {
public:
	ListNode* plusOne(ListNode* head) {
		vector<ListNode*> nodes;
		ListNode *current = head;
		while (current != NULL) {
			nodes.emplace_back(current);
			current = current -> next;
		}

		int temp = nodes.back() -> val + 1;
		int carry = temp / 10;
		nodes.back() -> val = temp % 10;
		for (int i = nodes.size() - 2; i >= 0 && carry != 0; i--) {
			temp = nodes[i] -> val + carry;
			carry = temp / 10;
			nodes[i] -> val = temp % 10;
		}

		if (carry != 0) {
			ListNode *newHead = new ListNode(carry);
			newHead -> next = head;
			return newHead;
		}
		else
			return head;
	}
};

// DFS by recursion
class Solution {
private:
	int dfs(ListNode *node) {
		if (node == NULL)
			return 1;

		if (dfs(node -> next) == 0)
			return 0;
		else {
			int temp = node -> val + 1;
			node -> val = temp % 10;
			return temp / 10;
		}
	}
public:
	ListNode* plusOne(ListNode* head) {
		if (dfs(head) == 0)
			return head;
		else {
			ListNode *newHead = new ListNode(1);
			newHead -> next = head;
			return newHead;
		}
	}
};