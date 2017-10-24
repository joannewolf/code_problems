#include <math.h>
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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* newHead = new ListNode(0), *current = newHead;
        for (int i = 0; i < lists.size(); i++) {
            if (lists[i] == NULL) {
                lists.erase(lists.begin() + i);
                i--;
            }
        }
        while (!lists.empty()) {
            int minMalue = INT_MAX, flag = -1;
            for (int i = 0; i < lists.size(); i++) {
                if (lists[i] -> val < minMalue) {
                    minMalue = lists[i] -> val;
                    flag = i;
                }
            }
            current -> next = lists[flag];
            if (lists[flag] -> next == NULL)
                lists.erase(lists.begin() + flag);
            else
                lists[flag] = lists[flag] -> next;
            current = current -> next;
        }
        return (newHead -> next);
    }
};