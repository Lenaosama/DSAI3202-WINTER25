from mpi4py import MPI
import socket
import time

def square(n):
    return n * n

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    hostname = socket.gethostname()

    n = int(1e8)  # Or increase to push bonus

    if rank == 0:
        start_time = time.time()

    # Divide work
    chunk_size = n // size
    start = rank * chunk_size + 1
    end = n if rank == size - 1 else (rank + 1) * chunk_size

    local_squares = [square(x) for x in range(start, end + 1)]
    local_count = len(local_squares)
    local_last = local_squares[-1]

    # Reduce results
    total_count = comm.reduce(local_count, op=MPI.SUM, root=0)
    max_square = comm.reduce(local_last, op=MPI.MAX, root=0)

    if rank == 0:
        end_time = time.time()
        print(f"Process {rank} on {hostname}: Total squares = {total_count}")
        print(f"Process {rank} on {hostname}: Max square = {max_square}")
        print(f"Process {rank} on {hostname}: Time taken = {end_time - start_time:.2f} seconds")
    else:
        print(f"Process {rank} on {hostname}: Computed {local_count} squares.")
