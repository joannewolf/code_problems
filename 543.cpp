#include <algorithm>
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
    int diameter = 0;
    int treeDepth(TreeNode* node) {
        if (node == NULL)
            return 0;
        if (node -> left == NULL && node -> right == NULL)
            return 1;
        int leftDepth = treeDepth(node -> left), rightDepth = treeDepth(node -> right);
        if (leftDepth + rightDepth > diameter)
            diameter = leftDepth + rightDepth;
        return max(leftDepth, rightDepth) + 1;
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        treeDepth(root);
        return diameter;
    }
};