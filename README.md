# DSAI3202-WINTER25
Parallel and distributed computing repository for labs and assignments. Created on 14/1/2025 by Lena Swaileh.

# DSAI 3202 – Lab 6: Distributed Square Calculation with MPI

## 👨‍💻 Objective
This lab demonstrates how to parallelize a computational task (squaring numbers from 1 to `n`) using the `mpi4py` library in Python. The implementation supports distributed execution across multiple machines, tracks which process ran on which host, and is optimized to scale to large values of `n`.

## 🧠 Concepts Used
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

---

### Install Requirements
Ensure `mpi4py` is installed on **all machines**:
```bash
pip install mpi4py

### Running the program
mpirun -np 4 --hostfile machines.txt python calculate_squares.py

