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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        vector<ListNode*> list;
        ListNode *current = head;
        while (current != NULL) {
        	list.push_back(current);
        	current = current -> next;
        }
        if (n == list.size())
        	return head -> next;
        else if (n == 1)
        	list[list.size() - 2] -> next = NULL;
        else
        	list[list.size() - n - 1] -> next = list[list.size() - n - 1] -> next -> next;
		return head;    	
    }
};