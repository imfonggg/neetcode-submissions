class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW, COL = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * COL for _ in range(ROW)]

        def dp(r, c):
            if r == ROW or c == COL or obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] != -1:
                return cache[r][c]
            if r == ROW -1 and c == COL - 1:
                return 1
            
            cache[r][c] = dp(r + 1,c) + dp(r, c + 1)
            return cache[r][c]

        return dp(0,0)