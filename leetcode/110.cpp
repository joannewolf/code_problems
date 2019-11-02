#include <stdlib.h>
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
    bool balanced = true;
    int treeDepth(TreeNode* node) {
        if (node == NULL)
            return 0;
        if (node -> left == NULL && node -> right == NULL)
            return 1;
        int leftDepth = treeDepth(node -> left);
        int rightDepth = treeDepth(node -> right);
        if (abs(leftDepth - rightDepth) > 1)
            balanced = false;
        return max(leftDepth, rightDepth) + 1;
    }
public:
    bool isBalanced(TreeNode* root) {
        treeDepth(root);
        return balanced;
    }
};