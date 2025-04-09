# DSAI3202-WINTER25
Parallel and distributed computing repository for labs and assignments. Created on 14/1/2025 by Lena Swaileh.

# DSAI 3202 – Lab 6: Distributed Square Calculation with MPI

## Objective
This lab demonstrates how to parallelize a computational task (squaring numbers from 1 to `n`) using the `mpi4py` library in Python. The implementation supports distributed execution across multiple machines, tracks which process ran on which host, and is optimized to scale to large values of `n`.

## Concepts Used
- Parallel and distributed computing
- MPI (Message Passing Interface)
- mpi4py (Python bindings for MPI)
- Hostname tracking using `socket.gethostname()`
- Performance measurement and scaling

---

## Files
- `calculate_squares.py`: Main Python script that distributes, computes, and collects squares across MPI processes.
- `machines.txt`: A text file listing the hostnames or IPs of machines used for MPI execution.
- `README.md`: This documentation file.

## Output
### n = 1e8
(base) student@vg-DSAI-3202-8:~$ mpirun -np 4 --hostfile machines.txt python DSAI3202-WINTER25/main.py
Process 3 on vg-DSAI-3202-8: Computed 25000000 squares.
Process 0 on vg-DSAI-3202-8: Total squares = 100000000
Process 0 on vg-DSAI-3202-8: Max square = 10000000000000000
Process 0 on vg-DSAI-3202-8: Time taken = 1.76 seconds
Process 2 on vg-DSAI-3202-8: Computed 25000000 squares.
Process 1 on vg-DSAI-3202-8: Computed 25000000 squares.
(base) student@vg-DSAI-3202-8:~$ mpirun -np 2 --hostfile machines.txt python DSAI3202-WINTER25/main.py
Process 0 on vg-DSAI-3202-8: Total squares = 100000000
Process 0 on vg-DSAI-3202-8: Max square = 10000000000000000
Process 0 on vg-DSAI-3202-8: Time taken = 3.36 seconds
Process 1 on vg-DSAI-3202-8: Computed 50000000 squares.

---

### Install Requirements
Ensure `mpi4py` is installed on **all machines**:
```bash
pip install mpi4py
```

### Running the program
mpirun -np 4 --hostfile machines.txt python main.py

