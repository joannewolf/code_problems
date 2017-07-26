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
    vector<long long> sum;
    vector<int> count;
    void calculateNode(int level, TreeNode *node) {
        if (node == NULL)
            return;
        int n = sum.size();
        if (level > n - 1) {
            sum.push_back(node -> val);
            count.push_back(1);
        }
        else {
            sum[level] += (node -> val);
            count[level] ++;
        }
        calculateNode(level + 1, node -> left);
        calculateNode(level + 1, node -> right);
    }
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> result;
        calculateNode(0, root);
        for (int i = 0; i < sum.size(); i++) {
            result.push_back((double)sum[i] / (double)count[i]);
        }
        return result;
    }
};