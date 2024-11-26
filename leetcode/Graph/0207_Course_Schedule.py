class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dependencies = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            dependencies[a].add(b)

        while True:
            current_courses = {i for i, prereq in dependencies.items() if not prereq}
            if not current_courses:
                break
            else:
                for i in current_courses:
                    dependencies.pop(i)
                for i, prereq in dependencies.items():
                    dependencies[i] -= current_courses

        if dependencies:
            return False
        else:
            return True
