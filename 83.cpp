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
    ListNode* deleteDuplicates(ListNode* head) {
    	if (head == NULL)
    		return head;

        ListNode *previous = head, *current = head -> next;
        while (current != NULL) {
        	if (current -> val == previous -> val)
        		previous -> next = current -> next;
        	else
        		previous = current;
        	current = current -> next;
        }
        return head;
    }
};