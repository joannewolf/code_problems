class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        if not folder:
            return []

        N = len(folder)
        folder.sort()
        result = [folder[0]]
        flag = 0
        for i in range(1, N):
            n = len(folder[flag])
            if (folder[i].startswith(folder[flag]) and
                folder[i][n] == '/'): # have to match the full folder name
                pass
            else:
                result.append(folder[i])
                flag = i

        return result
