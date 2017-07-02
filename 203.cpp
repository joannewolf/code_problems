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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode t(0);
        ListNode *temp = &t, *current = temp;
        temp -> next = head;
        while (current != NULL && current -> next != NULL) {
            printf("%d\n", current -> val);
            if (current -> next -> val == val)
                current -> next = current -> next -> next;
            else
                current = current -> next;
        }

        return temp -> next;
    }
};