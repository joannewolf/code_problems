class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        num_index = {}
        last_dup_index = -1
        current_sum = 0
        # add first k nums to num_dict
        for i in range(k):
            current_sum += nums[i]
            if nums[i] in num_index:
                last_dup_index = max(last_dup_index, num_index[nums[i]])
            num_index[nums[i]] = i

        result = current_sum if last_dup_index == -1 else 0
        for i in range(1, N - k + 1): # check subarray nums[i: i + k]
            # remove nums[i - 1] from num_dict
            current_sum -= nums[i - 1]
            # add nums[i + k - 1] to num_dict
            current_sum += nums[i + k - 1]
            if nums[i + k - 1] in num_index:
                last_dup_index = max(last_dup_index, num_index[nums[i + k - 1]])
            num_index[nums[i + k - 1]] = i + k - 1

            if last_dup_index < i:
                result = max(result, current_sum)

        return result
