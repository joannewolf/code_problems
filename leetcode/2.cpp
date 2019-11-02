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
        int carry = 0;
        ListNode *head = new ListNode(0), *current = head;
        while (l1 != NULL && l2 != NULL) {
            int temp = (l1 -> val) + (l2 -> val) + carry;
            carry = temp / 10;
            current -> next = new ListNode(temp % 10);
            current = current -> next;
            l1 = l1 -> next;
            l2 = l2 -> next;
        }
        while (l1 != NULL) {
            int temp = (l1 -> val) + carry;
            carry = temp / 10;
            current -> next = new ListNode(temp % 10);
            current = current -> next;
            l1 = l1 -> next;
        }
        while (l2 != NULL) {
            int temp = (l2 -> val) + carry;
            carry = temp / 10;
            current -> next = new ListNode(temp % 10);
            current = current -> next;
            l2 = l2 -> next;
        }
        if (carry != 0)
            current -> next = new ListNode(carry);
        return head -> next;
    }
};