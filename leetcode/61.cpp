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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL || head -> next == 0)
            return head;

        int length = 1;
        ListNode *current = head, *end, *newhead;
        while (current -> next != NULL) {
            length ++;
            current = current -> next;
        }
        end = current;

        k %= length;
        if (k == 0)
            return head;

        // rotate k rounds
        current = head;
        for (int i = 0; i < (length - k) - 1; i++)
            current = current -> next;
        newhead = current -> next;
        end -> next = head;
        current -> next = NULL;
        return newhead;
    }
};