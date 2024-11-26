class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        dependencies = {i: set() for i in range(numCourses)}
        for a, b in prerequisites:
            dependencies[a].add(b)

        courses = []
        while True:
            current_courses = {i for i, prereq in dependencies.items() if not prereq}
            if not current_courses:
                break
            else:
                courses.extend(list(current_courses))
                for i in current_courses:
                    dependencies.pop(i)
                for i, prereq in dependencies.items():
                    dependencies[i] -= current_courses

        if dependencies:
            return []
        else:
            return courses