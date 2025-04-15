import time
import pygame
from collections import deque
from typing import Tuple, List
from .constants import BLUE, WHITE, CELL_SIZE, WINDOW_SIZE

class Explorer:
    def __init__(self, maze, visualize: bool = False):
        self.maze = maze
        self.x, self.y = maze.start_pos
        self.direction = (1, 0)  # Start facing right
        self.moves = []
        self.start_time = None
        self.end_time = None
        self.visualize = visualize
        self.move_history = deque(maxlen=3)
        self.backtracking = False
        self.backtrack_path = []
        self.backtrack_count = 0  # Count number of backtrack operations
        
        # Enhancement: Dictionary to track how many times each cell is visited.
        self.visited_counts = {}
        
        if visualize:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption("Maze Explorer - Automated Solving")
            self.clock = pygame.time.Clock()
    
    def turn_right(self):
        x, y = self.direction
        self.direction = (-y, x)
    
    def turn_left(self):
        x, y = self.direction
        self.direction = (y, -x)
    
    def can_move_forward(self) -> bool:
        dx, dy = self.direction
        new_x, new_y = self.x + dx, self.y + dy
        return (0 <= new_x < self.maze.width and 
                0 <= new_y < self.maze.height and 
                self.maze.grid[new_y][new_x] == 0)
    
    def move_forward(self):
        """Move forward in the current direction and update visit count."""
        dx, dy = self.direction
        self.x += dx
        self.y += dy
        current_move = (self.x, self.y)
        self.moves.append(current_move)
        self.move_history.append(current_move)
        # Enhancement: Update the visited_counts dictionary for the new cell.
        self.visited_counts[current_move] = self.visited_counts.get(current_move, 0) + 1
        if self.visualize:
            self.draw_state()
    
    def is_stuck(self) -> bool:
        if len(self.move_history) < 3:
            return False
        return (self.move_history[0] == self.move_history[1] == self.move_history[2])
    
    def backtrack(self) -> bool:
        """Backtrack to a previous cell with more than one available move."""
        if not self.backtrack_path:
            self.backtrack_path = self.find_backtrack_path()
        if self.backtrack_path:
            next_pos = self.backtrack_path.pop()
            self.x, self.y = next_pos
            self.backtrack_count += 1
            if self.visualize:
                self.draw_state()
            return True
        return False
    
    def find_backtrack_path(self) -> List[Tuple[int, int]]:
        """Find a branching point to backtrack to."""
        path = []
        visited = set()
        for i in range(len(self.moves) - 1, -1, -1):
            pos = self.moves[i]
            if pos in visited:
                continue
            visited.add(pos)
            path.append(pos)
            if self.count_available_choices(pos) > 1:
                return path[::-1]
        return path[::-1]
    
    def count_available_choices(self, pos: Tuple[int, int]) -> int:
        """Count the number of available moves from a given cell."""
        x, y = pos
        choices = 0
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < self.maze.width and 
                0 <= new_y < self.maze.height and 
                self.maze.grid[new_y][new_x] == 0):
                choices += 1
        return choices
    
    def draw_state(self):
        """Draw the current state of the maze, start/end, and explorer."""
        self.screen.fill(WHITE)
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0),
                        (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (0, 255, 0), 
                         (self.maze.start_pos[0] * CELL_SIZE, self.maze.start_pos[1] * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), 
                         (self.maze.end_pos[0] * CELL_SIZE, self.maze.end_pos[1] * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, BLUE, 
                         (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        self.clock.tick(30)
    
    def print_statistics(self, time_taken: float):
        print("\n=== Maze Exploration Statistics ===")
        print(f"Total time taken: {time_taken:.2f} seconds")
        print(f"Total moves made: {len(self.moves)}")
        print(f"Number of backtrack operations: {self.backtrack_count}")
        print(f"Average moves per second: {len(self.moves)/time_taken:.2f}")
        print("==================================\n")
    
    def choose_best_direction(self):
        """
        Evaluate candidate directions (right, forward, left, back) and choose the one
        leading to the cell that has been visited the fewest times.
        """
        dx, dy = self.direction
        # Calculate candidate directions in a preferred order:
        right = (-dy, dx)
        forward = self.direction
        left = (dy, -dx)
        back = (-dx, -dy)
        candidate_directions = [right, forward, left, back]
        best_direction = None
        best_count = float('inf')
        for d in candidate_directions:
            new_x, new_y = self.x + d[0], self.y + d[1]
            if (0 <= new_x < self.maze.width and 0 <= new_y < self.maze.height and 
                self.maze.grid[new_y][new_x] == 0):
                count = self.visited_counts.get((new_x, new_y), 0)
                if count < best_count:
                    best_count = count
                    best_direction = d
        return best_direction
    
    def solve(self) -> Tuple[float, List[Tuple[int, int]]]:
        """
        Solve the maze using the enhanced algorithm.
        This method uses the right-hand rule with an added heuristic based on visit counts.
        If a cell has been visited more than a threshold (e.g., 3 times), it triggers backtracking.
        """
        self.start_time = time.time()
        # Mark the starting cell as visited.
        self.visited_counts[(self.x, self.y)] = 1
        if self.visualize:
            self.draw_state()
        
        while (self.x, self.y) != self.maze.end_pos:
            # Enhanced loop/dead-end detection:
            if self.visited_counts.get((self.x, self.y), 0) > 3:
                if not self.backtrack():
                    # If backtracking fails, turn around.
                    self.turn_left()
                    self.turn_left()
                    self.move_forward()
                continue
            
            # Use the heuristic to choose the best direction based on visit counts.
            candidate_direction = self.choose_best_direction()
            if candidate_direction is not None:
                self.direction = candidate_direction
                self.move_forward()
            else:
                # Fallback: if no candidate is found, backtrack or turn around.
                if not self.backtrack():
                    self.turn_left()
                    self.turn_left()
                    self.move_forward()
        
        self.end_time = time.time()
        time_taken = self.end_time - self.start_time
        
        if self.visualize:
            pygame.time.wait(2000)
            pygame.quit()
        
        self.print_statistics(time_taken)
        return time_taken, self.moves
