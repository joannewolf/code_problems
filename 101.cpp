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
    bool isSymmetricNode(TreeNode *left, TreeNode *right) {
        if (left == NULL && right == NULL)
            return true;
        else if ((left != NULL && right == NULL) || (left == NULL && right != NULL) || (left -> val != right -> val))
            return false;
        else
            return (isSymmetricNode(left -> left, right -> right) & isSymmetricNode(left -> right, right -> left));
    }
public:
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        return isSymmetricNode(root -> left, root -> right);
    }
};