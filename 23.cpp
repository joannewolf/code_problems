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
private:
    ListNode* merge2Lists(ListNode* &list1, ListNode* &list2) {
        ListNode* newHead = new ListNode(0), *current = newHead;
        while (list1 != NULL && list2 != NULL) {
            if (list1 -> val < list2 -> val) {
                current -> next = list1;
                list1 = list1 -> next;
            }
            else {
                current -> next = list2;
                list2 = list2 -> next;
            }
            current = current -> next;
        }
        if (list1 != NULL)
            current -> next = list1;
        else if (list2 != NULL)
            current -> next = list2;
        return (newHead -> next);
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.size() == 0)
            return NULL;
        while (lists.size() > 1){
            for (int i = 1; i < lists.size(); i ++) {
                lists[i - 1] = merge2Lists(lists[i], lists[i - 1]);
                lists.erase(lists.begin() + i);
            }
        }
        return lists[0];
    }
};