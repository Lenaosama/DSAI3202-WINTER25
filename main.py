"""
Main entry point for the maze runner game.
"""

import argparse
import multiprocessing
from src.game import run_game
from src.explorer import Explorer
from src.maze import create_maze

class SimpleMaze:
    """Lightweight maze class for parallel processing"""
    def __init__(self, grid, start, end, width, height):
        self.grid = grid
        self.start_pos = start
        self.end_pos = end
        self.width = width
        self.height = height

def run_explorer_task(config):
    """Task executed by each parallel explorer process"""
    try:
        # Reconstruct maze from config
        if config["type"] == "static":
            maze = create_maze(0, 0, "static")
        else:
            maze = SimpleMaze(
                config["grid"],
                config["start"],
                config["end"],
                config["width"],
                config["height"]
            )
        
        # Run exploration
        explorer = Explorer(maze, visualize=False)
        time_taken, moves = explorer.solve()
        return {
            "time": time_taken,
            "moves": len(moves),
            "backtracks": explorer.backtrack_count
        }
    except Exception as e:
        print(f"Explorer failed: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Maze Runner Game")
    parser.add_argument("--type", choices=["random", "static"], default="random",
                      help="Type of maze (random or static)")
    parser.add_argument("--width", type=int, default=30,
                      help="Maze width (ignored for static)")
    parser.add_argument("--height", type=int, default=30,
                      help="Maze height (ignored for static)")
    parser.add_argument("--auto", action="store_true",
                      help="Enable automated exploration")
    parser.add_argument("--visualize", action="store_true",
                      help="Enable visualization")
    parser.add_argument("--workers", type=int, default=4,
                      help="Number of parallel explorers")

    args = parser.parse_args()

    if args.auto:
        # Handle maze generation
        if args.type == "static":
            configs = [{"type": "static"}] * args.workers
        else:
            # Generate once and share configuration
            maze = create_maze(args.width, args.height, "random")
            config = {
                "type": "random",
                "grid": maze.grid,
                "start": maze.start_pos,
                "end": maze.end_pos,
                "width": maze.width,
                "height": maze.height
            }
            configs = [config] * args.workers

        # Run parallel explorers
        with multiprocessing.Pool(args.workers) as pool:
            results = pool.map(run_explorer_task, configs)

        # Filter failed results
        valid_results = [r for r in results if r is not None]
        
        if not valid_results:
            print("All explorers failed!")
            return

        # Find best performer
        best = min(valid_results, key=lambda x: x["moves"])
        
        # Print summary
        print("\n=== Exploration Results ===")
        print(f"Total explorers: {len(valid_results)}")
        print(f"Best time: {best['time']:.2f}s")
        print(f"Fewest moves: {best['moves']}")
        print(f"Backtracks: {best['backtracks']}")
        print("===========================")

    else:
        # Run interactive game
        run_game(
            maze_type=args.type,
            width=args.width,
            height=args.height
        )

if __name__ == "__main__":
    main()