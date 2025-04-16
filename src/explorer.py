import time
import pygame
from src.solvers.base_solver import BaseSolver
from src.solvers.bfs_solver import BFSSolver
from src.solvers.dfs_solver import DFSSolver
from src.solvers.astar_solver import AStarSolver
from src.solvers.rh_solver import RHSolver
from src.constants import BLUE, WHITE, BLACK, RED, GREEN, CELL_SIZE, WINDOW_SIZE

class Explorer:
    """
    The Explorer class serves as a controller for automated maze solving.
    It delegates the actual solving process to one of several algorithm-specific
    solvers, such as BFS, DFS, A*, or Right-Hand Rule, depending on the input.

    It also handles timing, statistics collection, and visualization
    of the explorer's path using Pygame.
    """

    def __init__(self, maze, algorithm='bfs', visualize=False):
        """
        Initialize the explorer with the chosen algorithm and maze.
        If visualization is enabled, Pygame is initialized to display the maze solving process.
        """
        self.maze = maze
        self.visualize = visualize
        self.algorithm = algorithm.lower()
        self.solver = self._create_solver()  # Select algorithm class
        self.moves = []  # Will store the final path through the maze
        self.statistics = {
            'time': 0,
            'moves': 0,
            'backtracks': 0
        }

        if visualize:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption(f"Maze Explorer - {self.algorithm.upper()}")
            self.clock = pygame.time.Clock()

    def _create_solver(self):
        """
        Internal factory method to select the appropriate solving algorithm.
        This keeps the Explorer class clean and decoupled from solver logic.
        """
        return {
            'bfs': BFSSolver,
            'dfs': DFSSolver,
            'astar': AStarSolver,
            'rh': RHSolver
        }[self.algorithm](self.maze)

    def solve(self):
        """
        Core method that runs the selected solver's logic and times its performance.
        It stores the resulting path, backtrack count, and total runtime.
        If visualization is enabled, it animates the path afterwards.
        """
        start_time = time.time()
        self.moves = self.solver.solve()  # Run selected algorithm
        self.statistics['time'] = time.time() - start_time
        self.statistics['moves'] = len(self.moves)
        self.statistics['backtracks'] = getattr(self.solver, 'backtrack_count', 0)

        if self.visualize:
            self._animate_path()
            pygame.quit()

        self._print_statistics()
        return self.statistics['time'], self.moves

    def _animate_path(self):
        """
        Displays the explorer moving through the maze in real time.
        Each cell in the solution path is drawn one-by-one, creating a smooth animation.
        """
        for x, y in self.moves:
            self._draw_state(x, y)
            time.sleep(0.01)  # Small delay for animation effect
            pygame.event.pump()  # Allow window to stay responsive

    def _draw_state(self, x, y):
        """
        Renders the full maze, including the walls, start and end points,
        and the current position of the explorer.
        This function is called repeatedly during animation.
        """
        self.screen.fill(WHITE)

        for row in range(self.maze.height):
            for col in range(self.maze
