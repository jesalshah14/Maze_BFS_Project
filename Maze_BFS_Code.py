
from  typing import List
import collections

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        dirs = [0, 1, 0, -1, 0]
        row, col = len(maze), len(maze[0])
		
        def bfs(i, j):
            queue = collections.deque([[i, j]])
            visited.add((i, j))
            while queue:
                i, j = queue.pop()
                if [i, j] == destination: return True
                for k in range(4):
                    move_i, move_j = i, j
                    while 0 <= (t1 := move_i + dirs[k]) < row and 0 <= (t2 := move_j + dirs[k + 1]) < col and maze[t1][t2] != 1:
                        move_i, move_j = t1, t2
                    if move_i == i and move_j == j: continue
                    if (move_i, move_j) not in visited:
                        visited.add((move_i, move_j))
                        queue.appendleft([move_i, move_j])
            return False

        return bfs(start[0], start[1])
    
# Test the input
maze = [[0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]]

start = [0, 4]
destination = [4, 4]
output = Solution()
print(output.hasPath(maze, start, destination))  # Output: True