import multiprocessing, time
from src.maze import create_maze
from src.explorer import Explorer

def run_explorer_instance(params):
    width, height, maze_type = params
    maze = create_maze(width, height, maze_type)
    explorer = Explorer(maze, visualize=False)
    start_time = time.time()
    _, moves = explorer.solve()
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, len(moves), explorer.backtrack_count

def run_multiple_explorers(num_explorers=4, maze_type="static", width=50, height=50): # changed this for question 3
    params = (width, height, maze_type)
    pool = multiprocessing.Pool(processes=num_explorers)
    results = pool.map(run_explorer_instance, [params] * num_explorers)
    pool.close()
    pool.join()
    print("\n=== Multi-Explorer Summary ===")
    for i, (t, moves, backtracks) in enumerate(results, start=1):
        print(f"Explorer {i}: Time={t:.2f}s, Moves={moves}, Backtracks={backtracks}")
    best = min(results, key=lambda x: x[1])  # Best based on move count, for instance
    print(f"\nBest Performance: Time={best[0]:.2f}s, Moves={best[1]}, Backtracks={best[2]}")

if __name__ == "__main__":
    run_multiple_explorers(num_explorers=4, maze_type="static")
