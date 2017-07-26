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
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.size() == 0)
            return NULL;
        if (nums.size() == 1) {
            TreeNode* root = new TreeNode(nums[0]);
            return root;
        }

        int half = nums.size() / 2;
        TreeNode* root = new TreeNode(nums[half]);
        vector<int> leftNums(nums.begin(), nums.begin() + half);
        vector<int> rightNums(nums.begin() + half + 1, nums.end());
        root -> left = sortedArrayToBST(leftNums);
        root -> right = sortedArrayToBST(rightNums);

        return root;
    }
};