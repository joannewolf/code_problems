/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

// O(NlogN) if tree is balanced, O(N^2) at worst, by recursion
class Solution {
public:
	TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
		if (nums.empty())
			return NULL;

		// find the max element in nums
		int maxIndex = distance(nums.begin(), max_element(nums.begin(), nums.end()));
		TreeNode *root = new TreeNode(nums[maxIndex]);
		vector<int> leftNums(nums.begin(), nums.begin() + maxIndex);
		vector<int> rightNums(nums.begin() + maxIndex + 1, nums.end());
		root -> left = constructMaximumBinaryTree(leftNums);
		root -> right = constructMaximumBinaryTree(rightNums);
		return root;
	}
};

// O(N)
// Scan numbers from left to right, build the tree one node by one step
// Use a stack to keep some (not all) tree nodes and ensure a decreasing order
// For each number, keep pop the stack until empty or a bigger number; 
// The bigger number (if exist, it will be still in stack) is current number’s root, and the last popped number (if exist) is current number’s right child (temporarily, this relationship may change in the future)
// Then we push current number into the stack.
class Solution {
public:
	TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
		vector<TreeNode*> nodeStack;
		for (int i = 0; i < nums.size(); i++) {
			TreeNode* current = new TreeNode(nums[i]);
			while (!nodeStack.empty() && nodeStack.back() -> val < nums[i]) {
				current -> left = nodeStack.back();
				nodeStack.pop_back();
			}
			if (!nodeStack.empty())
				nodeStack.back() -> right = current;
			nodeStack.emplace_back(current);
		}
		return nodeStack.front();
	}
};