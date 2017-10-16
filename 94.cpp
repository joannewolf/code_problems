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
    	if (root == NULL)
    		return vector<int>();
        if (root -> left == NULL && root -> right == NULL)
        	return vector<int>(1, root -> val);
		vector<int> leftResult = inorderTraversal(root -> left);
		vector<int> rightResult = inorderTraversal(root -> right);
		leftResult.push_back(root -> val);
		leftResult.insert(leftResult.end(), rightResult.begin(), rightResult.end());
		return leftResult;
    }
};