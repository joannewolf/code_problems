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
    ListNode* swapPairs(ListNode* head) {
    	if (head == NULL || head -> next == NULL)
    		return head;
        ListNode *newHead = new ListNode(0), *current = head, *previous = newHead;
        while (current != NULL && current -> next != NULL) {
        	ListNode *temp = current -> next;
        	current -> next = current -> next -> next;
        	temp -> next = current;
        	previous -> next = temp;
        	previous = current;
        	current = current -> next;
        }
        return newHead -> next;
    }
};