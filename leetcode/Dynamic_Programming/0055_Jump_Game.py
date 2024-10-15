# DP, backward
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        last_reachable = N - 1
        for i in range(N - 2, -1, -1):
            if i + nums[i] >= last_reachable:
                last_reachable = i

        return bool(nums[0] >= last_reachable)

# DP, iteration
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        can_reach = [-1] * N # -1 means unchecked, 0 means cannot reach end, 1 means can reach end
        can_reach[N - 1] = 1
        stack = [0]

        while stack:
            current = stack[-1]
            if can_reach[current] != -1:
                stack.pop()
            elif current + nums[current] >= N - 1:
                can_reach[current] = 1
                stack.pop()
            else:
                all_child_checked = True
                current_result = 0
                for i in range(1, nums[current] + 1):
                    if can_reach[current + i] == -1:
                        stack.append(current + i)
                        all_child_checked = False
                    else:
                        current_result |= can_reach[current + i]

                if all_child_checked:
                    can_reach[current] = current_result
                    stack.pop()

        return bool(can_reach[0])

# DP, recursion, MLE
class Solution(object):
    def __init__(self):
        self.can_reach = []

    def checkCanJump(self, nums, start):
        if self.can_reach[start] != -1:
            return self.can_reach[start]
        elif start + nums[start] >= len(nums) - 1:
            self.can_reach[start] = 1
            return 1
        else:
            result = 0
            for i in range(1, nums[start] + 1):
                if self.can_reach[start + i] != -1:
                    result |= self.can_reach[start + i]
                else:
                    result |= self.checkCanJump(nums, start + i)
            self.can_reach[start] = result
            return result

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        self.can_reach = [-1] * N # -1 means unchecked, 0 means cannot reach end, 1 means can reach end
        self.can_reach[N - 1] = 1

        return bool(self.checkCanJump(nums, 0))
