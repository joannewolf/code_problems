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
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        if (root -> left == NULL && root -> right == NULL)
            return 1;
        int result = -1;
        if (root -> left != NULL)
            result = max(result, maxDepth(root -> left) + 1);
        if (root -> right != NULL)
            result = max(result, maxDepth(root -> right) + 1);
        return result;
    }
};