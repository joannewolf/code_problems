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
    vector<int> inorderTraversal(TreeNode* root) {
    	vector<int> result;
    	stack<TreeNode*> toBeChecked;
    	TreeNode *current = root;
    	while (current != NULL || !toBeChecked.empty()) {
    		while (current != NULL) {
    			toBeChecked.push(current);
    			current = current -> left;
    		}
    		current = toBeChecked.top();
    		result.push_back(current -> val);
    		toBeChecked.pop();
    		current = current -> right;
    	}
    	return result;
    }
};