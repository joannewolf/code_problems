#include <algorithm>
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
        vector<ListNode*> A, B;
        ListNode *current;
        // save all nodes
        current = headA;
        while (current != NULL) {
            A.push_back(current);
            current = current -> next;
        }
        current = headB;
        while (current != NULL) {
            B.push_back(current);
            current = current -> next;
        }
        // find the intersection from tail
        if (A.size() == 0 || B.size() == 0 || A.back() != B.back())
            return NULL;
        for (int i = 0; i < min(A.size(), B.size()); i++) {
            if (A[A.size() - 1 - i] != B[B.size() - 1 - i])
                return A[A.size() - i];
        }
        return (A.size() < B.size()) ? A[0] : B[0];
    }
};