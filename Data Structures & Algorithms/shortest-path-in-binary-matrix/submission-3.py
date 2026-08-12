class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROW - 1][COL - 1] == 1:
            return -1
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length

                directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == ROW or nc == COL or grid[nr][nc] == 1 or (nr, nc) in visit:
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        
        return -1