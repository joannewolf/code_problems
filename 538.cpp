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
    int convert(int previousSum, TreeNode* node) {
        if (node == NULL)
            return 0;
        printf("%d %d\n", previousSum, node -> val);
        node -> val += previousSum;
        if (node -> left == NULL && node -> right == NULL)
            return (node -> val - previousSum);
        if (node -> right != NULL)
            node -> val += (convert(previousSum, node -> right));
        if (node -> left != NULL)
            return (node -> val + convert(node -> val, node -> left) - previousSum);
        return (node -> val - previousSum);
    }
public:
    TreeNode* convertBST(TreeNode* root) {
        convert(0, root);
        return root;
    }
};