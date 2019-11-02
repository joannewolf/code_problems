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
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        TreeNode* result;
        if (t1 == NULL && t2 == NULL)
            return NULL;
        else if (t1 == NULL && t2 != NULL) {
            result = t2;
            result -> left = mergeTrees(NULL, t2 -> left);
            result -> right = mergeTrees(NULL, t2 -> right);
        }
        else if (t1 != NULL && t2 == NULL) {
            result = t1;
            result -> left = mergeTrees(t1 -> left, NULL);
            result -> right = mergeTrees(t1 -> right, NULL);
        }
        else {
            result = t1;
            result -> val = (t1 -> val) + (t2 -> val);
            result -> left = mergeTrees(t1 -> left, t2 -> left);
            result -> right = mergeTrees(t1 -> right, t2 -> right);
        }
        return result;
    }
};