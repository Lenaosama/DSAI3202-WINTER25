import multiprocessing, time
from maze import create_maze
from explorer import Explorer

def run_explorer_instance(params):
    width, height, maze_type = params
    # Create the maze; for static mazes, width and height might be ignored.
    maze = create_maze(width, height, maze_type)
    # Create an explorer instance with visualization disabled.
    explorer = Explorer(maze, visualize=False)
    start_time = time.time()
    # Solve the maze; explorer.solve() returns a tuple (time_taken, moves)
    _, moves = explorer.solve()
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, len(moves), explorer.backtrack_count

def run_multiple_explorers(num_explorers=4, maze_type="static", width=50, height=50):
    params = (width, height, maze_type)
    pool = multiprocessing.Pool(processes=num_explorers)
    # Run the explorer on multiple processes using the same parameters.
    results = pool.map(run_explorer_instance, [params] * num_explorers)
    pool.close()
    pool.join()
    
    print("\n=== Multi-Explorer Summary ===")
    for i, (t, moves, backtracks) in enumerate(results, start=1):
        print(f"Explorer {i}: Time={t:.2f}s, Moves={moves}, Backtracks={backtracks}")
    
    best = min(results, key=lambda x: x[1])  # Best based on move count.
    print(f"\nBest Performance: Time={best[0]:.2f}s, Moves={best[1]}, Backtracks={best[2]}")

if __name__ == "__main__":
    print("Starting multi-explorer test...")
    run_multiple_explorers(num_explorers=4, maze_type="static")
