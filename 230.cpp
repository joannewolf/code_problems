#include <stack>
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
    int kthSmallest(TreeNode* root, int k) {
    	TreeNode *current = root;
    	stack<TreeNode*> st;
    	while (current != NULL || !st.empty()) {
    		while (current != NULL) {
    			st.push(current);
    			current = current -> left;
    		}
    		current = st.top();
    		st.pop();
    		k --;
    		if (k == 0)
    			return current -> val;
    		current = current -> right;
    	}
    }
};