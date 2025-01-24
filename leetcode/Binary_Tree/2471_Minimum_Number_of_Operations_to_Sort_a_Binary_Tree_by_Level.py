# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        result = 0
        current_level = [root]
        while current_level:
            nums = [node.val for node in current_level]
            result += self._min_swap_to_sort(nums)

            next_level = []
            for node in current_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current_level = next_level

        return result

    def _min_swap_to_sort(self, nums):
        # normalize num array to [0...N]
        nums = [(val, i) for i, val in enumerate(nums)]
        nums.sort()
        nums = [i for _, i in nums]

        count = 0
        N = len(nums)
        checked = set()
        for i in range(N):
            if i not in checked:
                temp_count = 1
                checked.add(i)
                start, current = i, nums[i]
                while current != start:
                    temp_count += 1
                    checked.add(current)
                    current = nums[current]

                count += (temp_count - 1)

        return count
