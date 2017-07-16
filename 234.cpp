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
    bool isPalindrome(ListNode* head) {
        vector<int> nums;
        ListNode *current = head;
        while (current != NULL) {
            nums.push_back(current -> val);
            current = current -> next;
        }
        for (int i = 0; i < nums.size() / 2; i++) {
            if (nums[i] != nums[nums.size() - 1 - i])
                return false;
        }
        return true;
    }
};