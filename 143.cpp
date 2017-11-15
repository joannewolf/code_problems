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
        // find the head of second half of the list
        ListNode *walk = head, *run = head;
        while (run != NULL && run -> next != NULL) {
            walk = walk -> next;
            run = run -> next -> next;
        }

        // reverse the second half of the list
        ListNode *previous = NULL, *current = walk;
        while (current != NULL) {
            ListNode *next = current -> next;
            current -> next = previous;
            previous = current;
            current = next;
        }

        // merge two halves of list
        current = head;
        ListNode *current2 = previous;
        while (current != NULL && current2 != NULL && current != current2) {
            ListNode *next = current -> next, *next2 = current2 -> next;
            current -> next = current2;
            if (current2 != next)
                current2 -> next = next;
            current = next;
            current2 = next2;
        }
    }
};