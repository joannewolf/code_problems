#include <stdlib.h>
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
    int totalTilt = 0;
    int treeSum(TreeNode* node) {
        if (node == NULL)
            return 0;
        if (node -> left == NULL && node -> right == NULL)
            return (node -> val);
        int leftSum = treeSum(node -> left);
        int rightSum = treeSum(node -> right);
        totalTilt += abs(leftSum - rightSum);
        return (leftSum + rightSum + (node -> val));
    }
public:
    int findTilt(TreeNode* root) {
        treeSum(root);
        return totalTilt;
    }
};