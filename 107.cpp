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
    vector<vector<int>> nodeList;
    void printOrder(int level, TreeNode *node) {
        if (node == NULL)
            return;
        if (nodeList.size() < level)
            nodeList.insert(nodeList.begin(), vector<int>());
        nodeList[nodeList.size() - level].push_back(node -> val);
        if (node -> left != NULL)
            printOrder(level + 1, node -> left);
        if (node -> right != NULL)
            printOrder(level + 1, node -> right);
    }
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        printOrder(1, root);
        return nodeList;
    }
};