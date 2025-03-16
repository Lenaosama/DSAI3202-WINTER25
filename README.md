# DSAI3202-WINTER25
Parallel and distributed computing repository for labs and assignments. Created on 14/1/2025 by Lena Swaileh.

# Project Title
Performance Comparison: Sequential Execution vs. Threads vs. Processes

# Description
This project explores the execution time and efficiency of different execution models in Python: sequential execution, multithreading, and multiprocessing. The goal is to analyze their performance differences for CPU-bound tasks.

# Features
Sequential execution for baseline performance
Multithreading implementation
Multiprocessing implementation
Performance metrics: execution time, speedup, and efficiency

# Results Summary
Multiprocessing achieved a 2.28x speedup and 57% efficiency, making it the best option for CPU-bound tasks.
Multithreading showed minimal improvement due to Python’s Global Interpreter Lock (GIL).

How to Run the Code:
python main.py
