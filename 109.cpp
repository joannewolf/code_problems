/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
	TreeNode* listToBST(ListNode* start, ListNode* end) {
		if (start == end)
			return NULL;

		ListNode *walk = start, *run = start;
		while (run != end && run -> next != end) {
			walk = walk -> next;
			run = run -> next -> next;
		}

		TreeNode* parent = new TreeNode(walk -> val);
		parent -> left = listToBST(start, walk);
		parent -> right = listToBST(walk -> next, end);

		return parent;
	}
public:
    TreeNode* sortedListToBST(ListNode* head) {
        if (head == NULL)
        	return NULL;
        else
        	return listToBST(head, NULL);
    }
};