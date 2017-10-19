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
public:
    bool isValidBST(TreeNode* root) {
    	if (root == NULL)
    		return true;
    	TreeNode *current = root, *previous = NULL;
    	stack<TreeNode*> st;
    	while (current != NULL || !st.empty()) {
    		while (current != NULL) {
    			st.push(current);
    			current = current -> left;
    		}
    		current = st.top();
    		st.pop();
    		if (previous != NULL && current -> val <= previous -> val)
    			return false;
    		previous = current;
    		current = current -> right;
    	}
    	return true;
    }
};