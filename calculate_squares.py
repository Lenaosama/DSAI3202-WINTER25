from mpi4py import MPI
import socket
import time

def square(n):
    return n * n

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    hostname = socket.gethostname()

    n = int(1e8)  # You can change this for bonus testing

    if rank == 0:
        start_time = time.time()
        numbers = range(1, n + 1)
        chunk_size = len(numbers) // size
        chunks = [range(i, min(i + chunk_size, n + 1)) for i in range(1, n + 1, chunk_size)]
    else:
        chunks = None
        start_time = None

    # Scatter the chunks to all processes
    local_chunk = comm.scatter(chunks, root=0)

    # Compute squares for the local chunk
    local_squares = [square(x) for x in local_chunk]

    # Gather results at the root process
    all_squares = comm.gather(local_squares, root=0)

    if rank == 0:
        final_squares = [item for sublist in all_squares for item in sublist]
        print(f"Process {rank} on {hostname}: Final squares count = {len(final_squares)}")
        print(f"Process {rank} on {hostname}: Last square = {final_squares[-1]}")
        end_time = time.time()
        print(f"Process {rank} on {hostname}: Time taken = {end_time - start_time:.2f} seconds")
    else:
        print(f"Process {rank} on {hostname}: Computed {len(local_squares)} squares.")
