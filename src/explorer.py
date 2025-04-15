"""
Maze Explorer module with multiple algorithms (Fixed Version)
"""

import time
import pygame
import heapq
from collections import deque
from typing import List, Tuple
from .constants import BLUE, WHITE, BLACK, RED, GREEN, CELL_SIZE, WINDOW_SIZE

class BaseSolver:
    """Base class for maze solving algorithms"""
    def __init__(self, maze):
        self.maze = maze
        self.visited = set()
        self.parent = {}
        self.backtrack_count = 0
        self.path = []

    def solve(self) -> List[Tuple[int, int]]:
        raise NotImplementedError

    def _reconstruct_path(self, end: Tuple[int, int]) -> List[Tuple[int, int]]:
        path = []
        current = end
        while current:
            path.append(current)
            current = self.parent.get(current)
        return path[::-1]

    def _is_valid(self, x: int, y: int) -> bool:
        return (0 <= x < self.maze.width and 
                0 <= y < self.maze.height and
                self.maze.grid[y][x] == 0)

class BFSSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.queue = deque()

    def solve(self):
        self.queue.append(self.maze.start_pos)
        self.visited.add(self.maze.start_pos)

        while self.queue:
            current = self.queue.popleft()
            if current == self.maze.end_pos:
                return self._reconstruct_path(current)
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = current[0]+dx, current[1]+dy
                if self._is_valid(nx, ny) and (nx, ny) not in self.visited:
                    self.visited.add((nx, ny))
                    self.parent[(nx, ny)] = current
                    self.queue.append((nx, ny))
        return []

class DFSSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.stack = []

    def solve(self):
        self.stack.append(self.maze.start_pos)
        self.visited.add(self.maze.start_pos)

        while self.stack:
            current = self.stack.pop()
            if current == self.maze.end_pos:
                return self._reconstruct_path(current)
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = current[0]+dx, current[1]+dy
                if self._is_valid(nx, ny) and (nx, ny) not in self.visited:
                    self.visited.add((nx, ny))
                    self.parent[(nx, ny)] = current
                    self.stack.append((nx, ny))
        return []

class AStarSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.open_set = []

    def solve(self):
        start = self.maze.start_pos
        end = self.maze.end_pos
        heapq.heappush(self.open_set, (0, start))
        g_score = {start: 0}
        self.parent = {start: None}

        while self.open_set:
            current = heapq.heappop(self.open_set)[1]
            if current == end:
                return self._reconstruct_path(end)
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                neighbor = (current[0]+dx, current[1]+dy)
                if self._is_valid(*neighbor):
                    tentative_g = g_score[current] + 1
                    if tentative_g < g_score.get(neighbor, float('inf')):
                        self.parent[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + self._heuristic(neighbor, end)
                        heapq.heappush(self.open_set, (f_score, neighbor))
        return []

    def _heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

class RHSolver(BaseSolver):
    def __init__(self, maze):
        super().__init__(maze)
        self.direction = (1, 0)
        self.move_history = deque(maxlen=3)
        self.backtrack_path = []

    def solve(self):
        current = self.maze.start_pos
        self.visited.add(current)
        self.path = [current]

        while current != self.maze.end_pos:
            next_pos = self._get_next_position(current)
            if next_pos:
                current = next_pos
                self.path.append(current)
                self.move_history.append(current)
                self.backtrack_path = []
            else:
                if not self._backtrack():
                    break
                current = self.backtrack_path.pop()
                self.path.append(current)
                self.backtrack_count += 1
        return self.path

    def _get_next_position(self, current):
        directions = [(-self.direction[1], self.direction[0]),
                      self.direction,
                      (self.direction[1], -self.direction[0])]
        
        for d in directions:
            nx, ny = current[0]+d[0], current[1]+d[1]
            if self._is_valid(nx, ny) and (nx, ny) not in self.visited:
                self.direction = d
                self.visited.add((nx, ny))
                return (nx, ny)
        return None

    def _backtrack(self):
        for i in range(len(self.path)-1, -1, -1):
            pos = self.path[i]
            if self._count_choices(pos) > 1:
                self.backtrack_path = self.path[i+1:]
                return True
        return False

    def _count_choices(self, pos):
        x, y = pos
        return sum(1 for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]
                  if self._is_valid(x+dx, y+dy))

class Explorer:
    def __init__(self, maze, algorithm='bfs', visualize=False):
        self.maze = maze
        self.algorithm = algorithm.lower()
        self.visualize = visualize
        self.solver = self._create_solver()
        self.moves = []
        self.backtrack_count = self.solver.backtrack_count 
        self.statistics = {
            'time': 0.0,
            'moves': 0,
            'backtracks': 0
        }

        if visualize:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            self.clock = pygame.time.Clock()

    def _create_solver(self):
        return {
            'bfs': BFSSolver,
            'dfs': DFSSolver,
            'astar': AStarSolver,
            'rh': RHSolver
        }[self.algorithm](self.maze)

    def solve(self):
        start_time = time.time()
        try:
            self.moves = self.solver.solve()
            self.statistics['time'] = time.time() - start_time or 0.001  # Prevent division by zero
            self.statistics['moves'] = len(self.moves)
            self.statistics['backtracks'] = self.solver.backtrack_count
        except Exception as e:
            print(f"Explorer failed: {str(e)}")
        
        if self.visualize:
            self._animate_path()
            pygame.quit()
        
        self._print_statistics()
        return self.statistics['time'], self.moves

    def _animate_path(self):
        for x, y in self.moves:
            self._draw_state(x, y)
            time.sleep(0.01)
            pygame.event.pump()

    def _draw_state(self, x: int, y: int):
        self.screen.fill(WHITE)
        # Draw maze walls
        for row in range(self.maze.height):
            for col in range(self.maze.width):
                if self.maze.grid[row][col] == 1:
                    pygame.draw.rect(self.screen, BLACK,
                                   (col*CELL_SIZE, row*CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE))
        # Draw start/end
        pygame.draw.rect(self.screen, GREEN,
                        (self.maze.start_pos[0]*CELL_SIZE,
                         self.maze.start_pos[1]*CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, RED,
                        (self.maze.end_pos[0]*CELL_SIZE,
                         self.maze.end_pos[1]*CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        # Draw current position
        pygame.draw.rect(self.screen, BLUE,
                        (x*CELL_SIZE, y*CELL_SIZE,
                         CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        self.clock.tick(60)



    def _print_statistics(self):
        print(f""\n=== Maze Exploration Statistics ==="")
        print(f"Total time taken: {self.statistics['time']:.2f}s")
        print(f"Total moves made: {self.statistics['moves']}")
        print(f"Number of backtrack operations: {self.statistics['backtracks']}")
        print(f"Average moves per second: {self.statistics['moves']/self.statistics['time']:.2f}")
        print("==================================\n")
