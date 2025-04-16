import argparse
import multiprocessing
from src.game import run_game
from src.explorer import Explorer
from src.maze import create_maze

# Simple wrapper class used to pass maze layout and metadata
# across processes when solving random mazes. This helps each
# process recreate the same maze, ensuring fair comparison.
class SimpleMaze:
    def __init__(self, grid, start, end, width, height):
        self.grid = grid
        self.start_pos = start
        self.end_pos = end
        self.width = width
        self.height = height

# Worker function to run one automated explorer instance.
# This function will be executed by multiple processes.
def run_explorer_task(config):
    try:
        # Depending on maze type, either regenerate static maze
        # or reconstruct shared random maze from passed config.
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

        # Run the explorer without visualization for speed
        explorer = Explorer(maze, visualize=False)
        time_taken, moves = explorer.solve()

        # Return relevant stats (used later to identify best result)
        return {
            "time": time_taken,
            "moves": len(moves),
            "backtracks": explorer.backtrack_count
        }
    except Exception as e:
        print(f"Explorer failed: {str(e)}")
        return None

# Main function: parses arguments, runs interactive or automated version
def main():
    parser = argparse.ArgumentParser(description="Maze Runner Game")
    parser.add_argument("--type", choices=["random", "static"], default="random")
    parser.add_argument("--width", type=int, default=30)
    parser.add_argument("--height", type=int, default=30)
    parser.add_argument("--auto", action="store_true")
    parser.add_argument("--visualize", action="store_true")
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    if args.auto:
        # If using static maze, we don't need to pass dimensions.
        # If using random maze, generate once and reuse for all processes.
        if args.type == "static":
            configs = [{"type": "static"}] * args.workers
        else:
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

        # Use a multiprocessing pool to execute parallel maze solving
        # Each worker will independently solve the maze and return results
        with multiprocessing.Pool(args.workers) as pool:
            results = pool.map(run_explorer_task, configs)

        # Clean up and analyze only successful results
        valid_results = [r for r in results if r is not None]
        if not valid_results:
            print("All explorers failed!")
            return

        # Select the best performer based on fewest moves
        best = min(valid_results, key=lambda x: x["moves"])

        print("\n=== Exploration Results ===")
        print(f"Total explorers: {len(valid_results)}")
        print(f"Best time: {best['time']:.2f}s")
        print(f"Fewest moves: {best['moves']}")
        print(f"Backtracks: {best['backtracks']}")
        print("===========================")
    else:
        # In interactive mode, the user plays using arrow keys
        run_game(maze_type=args.type, width=args.width, height=args.height)

if __name__ == "__main__":
    main()
