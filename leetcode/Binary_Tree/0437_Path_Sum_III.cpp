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
    int findPathSum(vector<int> sum, TreeNode* node, int target) {
        if (node == NULL)
            return 0;
        int count = 0;
        for (int i = 0; i < sum.size(); i++) {
            sum[i] += (node -> val);
            if (sum[i] == target)
                count ++;
        }
        sum.push_back(node -> val);
        if (node -> val == target)
            count ++;
        if (node -> left == NULL && node -> right == NULL)
            return count;
        else
            return count + findPathSum(sum, node -> left, target) + findPathSum(sum, node -> right, target);
    }
public:
    int pathSum(TreeNode* root, int sum) {
        if (root == NULL)
            return 0;
        return findPathSum(vector<int>(), root, sum);
    }
};