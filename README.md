# DSAI3202-WINTER25
Parallel and distributed computing repository for labs and assignments. Created on 14/1/2025 by Lena Swaileh.

## Square program

### **Purpose**
Compares sequential and parallel execution for computing squares of numbers.

### **Functions:**
- sequential_execution: Computes squares sequentially.
- multiprocessing_individual: Uses a fixed number of processes.
- multiprocessing_pool: Uses Pool.map and Pool.apply_async.
- multiprocessing_futures: Uses ProcessPoolExecutor.

### **Main Script:**
Tests with 1 million and 10 million numbers.

### **Output:**
=== Running Process Synchronization with Semaphores ===
Process Process-2:1 acquired connection 0
Process Process-3:1 acquired connection 1
Process Process-4:1 acquired connection 2
Process Process-2:2 released connection 0
Process Process-5:1 acquired connection 0
Process Process-3:2 released connection 1
Process Process-6:1 acquired connection 1
Process Process-4:2 released connection 2
Process Process-7:1 acquired connection 2
Process Process-5:2 released connection 0
Process Process-6:2 released connection 1
Process Process-9:1 acquired connection 0
Process Process-8:1 acquired connection 1
Process Process-7:2 released connection 2
Process Process-10:1 acquired connection 2
Process Process-9:2 released connection 0
Process Process-11:1 acquired connection 0
Process Process-8:2 released connection 1
Process Process-10:2 released connection 2
Process Process-11:2 released connection 0
All processes completed.

### **Conclusions**  
Process synchronization using semaphores effectively managed resource allocation, ensuring controlled access to limited connections. The execution followed an orderly pattern where each process acquired and released connections sequentially. Processes successfully acquired available connections, as seen with Process-2, Process-3, and Process-4 securing connections 0, 1, and 2 initially. As they released connections, subsequent processes, such as Process-5, Process-6, and Process-7, utilized the freed resources. This pattern continued until all processes completed execution.  

### **Key Takeaways**  
Semaphores efficiently regulated resource access among multiple processes, ensuring that connections were consistently allocated and released without deadlocks. The structured execution allowed all processes to complete without conflicts, demonstrating the importance of controlled resource management in concurrent applications. Proper synchronization mechanisms like semaphores prevent excessive contention and ensure smooth execution in multi-process environments.


## Process Synchronization with Semaphores 

### **Purpose**
Simulates a connection pool for database connections using semaphores to limit concurrent access.

### **Code Overview**
**`ConnectionPool` Class**:
  - Manages connections with `get_connection` and `release_connection` methods.
**`access_database` Function**:
  - Simulates a process acquiring, using, and releasing a connection.
    
### **Main Script**:
Creates a pool of 3 connections and spawns 10 processes to access them.

### **Answers:**  
When more processes try to access the pool than available connections, only three can acquire a connection at a time (`POOL_SIZE = 3`), while others wait. The semaphore controls access, ensuring that a new process acquires a connection only when another releases it. The output shows processes 2, 3, and 4 getting connections first, followed by process 6 when process 2 releases its connection.  

The semaphore prevents race conditions by limiting simultaneous access to the shared resource. It acts as a lock, ensuring only three processes use connections at once, while `Manager().list` maintains a shared, thread-safe list of available connections. The output confirms an orderly acquisition and release of connections without conflicts.  

### **Conclusion**  
The program successfully demonstrates **process synchronization using semaphores** for managing a limited connection pool. It ensures stable system performance when multiple processes (10) compete for a limited resource (3 connections). The semaphore prevents race conditions, enforces orderly access, and ensures that no two processes use the same connection at the same time. This method is effective for managing shared resources efficiently in multiprocessing environments.


## To run both at same time: 
`python main.py`
