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
    void reorderList(ListNode* head) {
    	if (head == NULL || head -> next == NULL)
    		return;
        int n = 0, flag = 0;
        ListNode *current = head, *previous = NULL, *next, *current2;
        // count the length of list
        while (current != NULL) {
        	n ++;
        	current = current -> next;
        }
        current = head;

        // find the second half of the list
        current2 = head;
        while (flag < n / 2) {
        	previous = current2;
        	current2 = current2 -> next;
        	flag ++;
        }
        previous -> next = NULL;
        printf("%d %d\n", previous -> val, current2 -> val);
        // reverse the second half of the list
        previous = NULL;
        next = current2 -> next;
        while (next != NULL) {
        	current2 -> next = previous;
        	previous = current2;
        	current2 = next;
        	next = next -> next;
        }
        current2 -> next = previous;

		// merge two halves of list
        while (current != NULL && current2 != NULL) {
        	ListNode *temp = current -> next, *temp2 = current2 -> next;
        	current -> next = current2;
        	if (temp != NULL)
        		current2 -> next = temp;
        	current = temp;
        	current2 = temp2;
        }
    }
};