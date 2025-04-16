import multiprocessing
import time
from src.maze import create_maze
from src.explorer import Explorer

# This function serves as the worker process for each explorer.
# It receives a tuple of parameters (width, height, maze_type),
# creates a maze using these parameters, and runs a single Explorer instance.
# It then returns the time taken, number of moves, and backtrack count.
def run_explorer_instance(params):
    width, height, maze_type = params

    # Generate the maze — random or static depending on the type
    maze = create_maze(width, height, maze_type)

    # Create an Explorer and disable visualization to keep it fast
    explorer = Explorer(maze, visualize=False)

    # Start the timer and solve the maze
    start_time = time.time()
    _, moves = explorer.solve()
    end_time = time.time()

    # Return key performance metrics
    total_time = end_time - start_time
    return total_time, len(moves), explorer.backtrack_count

# This function manages multiple explorers running in parallel.
# It uses the multiprocessing module to simulate several explorers
# solving the maze simultaneously — useful for benchmarking and comparison.
def run_multiple_explorers(num_explorers=4, maze_type="static", width=50, height=50):
    """
    Launch multiple explorers in parallel using the same maze configuration.
    This helps determine consistency, performance, and best-performing explorers.
    """
    # Parameters to pass to each process
    params = (width, height, maze_type)

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_explorers)

    # Map the same task across all workers (explorers)
    results = pool.map(run_explorer_instance, [params] * num_explorers)

    # Close and join the pool to free resources
    pool.close()
    pool.join()

    # Print out the performance of each explorer
    print("\n=== Multi-Explorer Summary ===")
    for i, (t, moves, backtracks) in enumerate(results, start=1):
        print(f"Explorer {i}: Time={t:.2f}s, Moves={moves}, Backtracks={backtracks}")

    # Find and display the best performance (based on fewest moves)
    best = min(results, key=lambda x: x[1])
    print(f"\nBest Performance: Time={best[0]:.2f}s, Moves={best[1]}, Backtracks={best[2]}")

# If this script is run directly, run the function with default settings
if __name__ == "__main__":
    run_multiple_explorers(num_explorers=4, maze_type="static")
