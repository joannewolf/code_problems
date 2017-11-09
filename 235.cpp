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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root == NULL)
            return root;

        TreeNode* current = root;
        int smallerVal = min(p -> val, q -> val), biggerVal = max(p -> val, q -> val);
        while (current != NULL) {
            if (current -> val <= biggerVal && current -> val >= smallerVal)
                return current;
            else if (current -> val < smallerVal)
                current = current -> right;
            else
                current = current -> left;
        }
    }
};