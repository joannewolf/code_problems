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
        if (head == NULL || head -> next == NULL)
            return head;
        ListNode blank(0), *newhead = &blank;
        ListNode *current = head, *previous = newhead;

        newhead -> next = head;
        while (current != NULL) {
            if (current -> next != NULL && current -> val == current -> next -> val) {
                int flag = current -> val;
                while (current != NULL && current -> val == flag)
                    current = current -> next;
                previous -> next = current;
            }
            else {
                previous -> next = current;
                previous = previous -> next;
                current = current -> next;
            }
        }
        return newhead -> next;
    }
};