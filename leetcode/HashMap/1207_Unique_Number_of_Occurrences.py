class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num_dict = {}
        for num in arr:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        occurrences = num_dict.values()
        return len(occurrences) == len(set(occurrences))
