class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        fresh = 0
        minutes = 0
        direction = [[0,1],[1,0],[0,-1],[-1,0]]

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1


        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc, in direction:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr == ROW or nc == COL or (nr,nc) in visit or grid[nr][nc] == 0:
                        continue
                
                    queue.append((nr,nc))
                    visit.add((nr,nc))
                    fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1