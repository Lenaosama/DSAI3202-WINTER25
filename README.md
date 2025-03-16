# DSAI3202-WINTER25
Parallel and distributed computing repository for labs and assignments. Created on 14/1/2025 by Lena Swaileh.

### **Conclusions**  

Sequential execution was the fastest for small datasets, taking 0.0843 seconds for 1 million numbers and 0.5192 seconds for 10 million. It has no overhead from managing processes but slows down with larger datasets. Multiprocessing with fixed processes improved performance for large datasets, running in 0.1424 seconds for 1 million numbers and 1.0806 seconds for 10 million, though it was slower for small ones due to process creation overhead. `Pool.map` had similar results, taking 0.1801 seconds for 1 million and 1.2370 seconds for 10 million, with slight overhead from managing the worker pool.  

In contrast, `apply_async` was much slower, requiring 52.5729 seconds for 1 million and 526.2259 seconds for 10 million due to high task management overhead. `ProcessPoolExecutor` was the worst, taking 107.3116 seconds for 1 million and failing for 10 million because of excessive resource usage.  

### **Key Takeaways**  

Sequential execution is best for small datasets. For large datasets, multiprocessing with fixed processes (0.1424s for 1M, 1.0806s for 10M) or `Pool.map` (0.1801s for 1M, 1.2370s for 10M) is most efficient. Asynchronous methods like `apply_async` (52.5729s for 1M, 526.2259s for 10M) and `ProcessPoolExecutor` (107.3116s for 1M, failed for 10M) add too much overhead and should be avoided. Large datasets require careful resource management.






### **Answers and Conclusion**  

When more processes try to access the pool than available connections, only three can acquire a connection at a time (`POOL_SIZE = 3`), while others wait. The semaphore controls access, ensuring that a new process acquires a connection only when another releases it. The output shows processes 2, 3, and 4 getting connections first, followed by process 6 when process 2 releases its connection.  

The semaphore prevents race conditions by limiting simultaneous access to the shared resource. It acts as a lock, ensuring only three processes use connections at once, while `Manager().list` maintains a shared, thread-safe list of available connections. The output confirms an orderly acquisition and release of connections without conflicts.  

### **Conclusion**  

The program successfully demonstrates **process synchronization using semaphores** for managing a limited connection pool. It ensures stable system performance when multiple processes (10) compete for a limited resource (3 connections). The semaphore prevents race conditions, enforces orderly access, and ensures that no two processes use the same connection at the same time. This method is effective for managing shared resources efficiently in multiprocessing environments.


to run both at same time: 
python main.py
