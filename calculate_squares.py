from mpi4py import MPI

def square(n):
    return n * n

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        # Define the range of numbers
        n = 100  # Example value
        numbers = range(1, n + 1)
        chunk_size = len(numbers) // size
        chunks = [numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size)]
    else:
        chunks = None

    # Scatter the chunks to all processes
    local_chunk = comm.scatter(chunks, root=0)

    # Compute squares for the local chunk
    local_squares = [square(x) for x in local_chunk]

    # Gather results at the root process
    all_squares = comm.gather(local_squares, root=0)

    if rank == 0:
        # Flatten the list of squares
        final_squares = [item for sublist in all_squares for item in sublist]
        print(f"Final squares: {final_squares}")
        print(f"Last square: {final_squares[-1]}")
