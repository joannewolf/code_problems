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
    vector<int> preorderTraversal(TreeNode* root) {
    	if (root == NULL)
    		return vector<int>();
    	vector<int> result;
    	stack<TreeNode*> st; 
    	st.push(root);
    	while (!st.empty()) {
    		TreeNode *temp = st.top();
    		st.pop();
    		result.push_back(temp -> val);
    		if (temp -> right != NULL)
    			st.push(temp -> right);
    		if (temp -> left != NULL)
    			st.push(temp -> left);
    	}
        return result;
    }
};