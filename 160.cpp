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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *current1 = headA, *current2 = headB;
        // current1: A -> B, current2: B -> A, they will be same length and intersection will be at same number of node
        while (current1 != current2) {
            current1 = (current1 != NULL) ? current1 -> next : headB;
            current2 = (current2 != NULL) ? current2 -> next : headA;
        }
        return current1;
    }
};