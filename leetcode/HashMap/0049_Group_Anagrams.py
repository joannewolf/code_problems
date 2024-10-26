class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        N = len(strs)
        str_dict = {}
        for i in range(N):
            # sort string and use it as dict key
            chars = ''.join(sorted(strs[i]))
            if chars not in str_dict:
                str_dict[chars] = [i]
            else:
                str_dict[chars].append(i)

        result = []
        for key, index in str_dict.items():
            group = [strs[i] for i in index]
            result.append(group)

        return result
