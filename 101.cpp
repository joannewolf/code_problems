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
    bool isSymmetric(TreeNode* root) {
        if (root == NULL)
            return true;
        stack<TreeNode*> left, right;

        if (root -> left == NULL && root -> right == NULL)
            return true;
        else if (root -> left != NULL && root -> right != NULL) {
            left.push(root -> left);
            right.push(root -> right);
        }
        else
            return false;

        while (!left.empty() && !right.empty()) {
            if (left.top() -> val != right.top() -> val)
                return false;
            else {
                TreeNode *tempLeft = left.top(), *tempRight = right.top();
                left.pop();
                right.pop();
                if (tempLeft -> left != NULL && tempRight -> right != NULL) {
                    left.push(tempLeft -> left);
                    right.push(tempRight -> right);
                }
                else if ((tempLeft -> left == NULL) != (tempRight -> right == NULL))
                    return false;
                if (tempLeft -> right != NULL && tempRight -> left != NULL) {
                    left.push(tempLeft -> right);
                    right.push(tempRight -> left);
                }
                else if ((tempLeft -> right == NULL) != (tempRight -> left == NULL))
                    return false;
            }
        }
        return true;
    }
};