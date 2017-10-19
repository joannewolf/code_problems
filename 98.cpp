#include <math.h>
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
	bool isValid(TreeNode* node, long long min_value, long long max_value) {
		if (node == NULL)
			return true;
		if ((long long)(node -> val) <= min_value || (long long)(node -> val) >= max_value)
			return false;
		return (isValid(node -> left, min_value, node -> val) & isValid(node -> right, node -> val, max_value));
	}
public:
    bool isValidBST(TreeNode* root) {
    	return isValid(root, LLONG_MIN, LLONG_MAX);
    }
};