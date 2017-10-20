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
        vector<int> leftResult = preorderTraversal(root -> left);
        vector<int> rightResult = preorderTraversal(root -> right);
        leftResult.insert(leftResult.begin(), root -> val);
        leftResult.insert(leftResult.end(), rightResult.begin(), rightResult.end());
        return leftResult;
    }
};