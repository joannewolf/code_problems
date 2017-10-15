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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> num1, num2;
        ListNode *current = l1;
        int carry = 0;
        while (current != NULL) {
        	num1.push(current -> val);
        	current = current -> next;
        }
        current = l2;
        while (current != NULL) {
        	num2.push(current -> val);
        	current = current -> next;
        }
        current = new ListNode(0);
        while (!num1.empty() || !num2.empty()) {
        	int num = carry;
        	if (!num1.empty()) {
        		num += num1.top();
        		num1.pop();
        	}
        	if (!num2.empty()) {
        		num += num2.top();
        		num2.pop();
        	}
        	carry = num / 10;
        	current -> val = num % 10;
        	ListNode *previous = new ListNode(0);
        	previous -> next = current;
        	current = previous;
        }
        if (carry != 0)
        	current -> val = carry;
        else
        	current = current -> next;
        return current;
    }
};