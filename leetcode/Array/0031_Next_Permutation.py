class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        # searching from tail, find the first decrease, meaning there's a possible larger permutation
        flag = -1
        for i in range(N - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                flag = i - 1
                break

        # print('flag', flag)
        if flag == -1:
            # means nums = [N, N-1, ..., 1]
            nums.sort()
        else:
            x = nums[flag]
            nums[flag:] = sorted(nums[flag:])
            for i in range(flag, N):
                if nums[i] > x:
                    y = nums.pop(i)
                    nums.insert(flag, y)
                    break
