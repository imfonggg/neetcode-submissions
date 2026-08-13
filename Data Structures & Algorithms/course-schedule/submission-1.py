class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        visit = set()

        def dfs(course):
            if course in visit:
                return False
            if prereqMap[course] == []:
                return True

            visit.add(course)
            for req in prereqMap[course]:
                if not dfs(req):
                    return False
            
            visit.remove(course)
            prereqMap[course] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
