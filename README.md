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
=== Running Square Program ===
Running test with 1000000 numbers...
Sequential for loop time: 0.0718 seconds
Multiprocessing separate process time: 0.0969 seconds
Multiprocessing pool map() time: 0.0918 seconds
Multiprocessing pool apply() time: 159.5040 seconds
ProcessPoolExecutor time: 106.4148 seconds

Running tests with 10 million numbers...
Sequential for loop time: 0.6453 seconds
Multiprocessing separate process time: 0.8586 seconds
Multiprocessing pool map() time: 0.8236 seconds

### Key Takeaways:
1. **Sequential for loop** is the fastest for both 1,000,000 and 10,000,000 numbers. With 1,000,000 numbers, it took 0.0718 seconds, and with 10,000,000 numbers, it took 0.6453 seconds.
2. **Multiprocessing pool map()** was the second fastest for both test cases. It took 0.0918 seconds for 1,000,000 numbers and 0.8236 seconds for 10,000,000 numbers.
3. **Multiprocessing separate process** was slightly slower, taking 0.0969 seconds for 1,000,000 numbers and 0.8586 seconds for 10,000,000 numbers.
4. **Multiprocessing pool apply()** had a significant performance hit, taking 159.5040 seconds for 1,000,000 numbers and was much slower than other methods.
5. **ProcessPoolExecutor** took 106.4148 seconds for 1,000,000 numbers, making it slower than the pool map method but more efficient than apply().

### Conclusion:
For 1,000,000 and 10,000,000 numbers, the **sequential for loop** performs best for smaller datasets, while the **multiprocessing pool map()** method is more efficient for larger datasets. The **multiprocessing pool apply()** method and **ProcessPoolExecutor** both showed significantly slower times, with the latter being more efficient than `apply()`. Asynchronous execution could potentially improve performance by reducing waiting times and allowing more concurrent tasks.


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

### **Answers:**  
1. **What happens if more processes try to access the pool than there are available connections?**
  If more processes try to access the pool than there are available connections, the semaphore ensures that only a limited number of processes can acquire connections at any given time. The excess processes will have to wait until a connection is released. This prevents processes from accessing the pool concurrently beyond the capacity, ensuring that no more than the allowed number of processes use the resources.

2. **How does the semaphore prevent race conditions and ensure safe access to the connections?**
  The semaphore is used to control access to the connection pool, allowing only a limited number of processes to acquire a connection. When a process tries to acquire a connection, it must first acquire the semaphore. If the semaphore count is zero (indicating no available connections), the process is blocked until another process releases a connection, which increments the semaphore count. By using the semaphore to limit concurrent access, race conditions are prevented because only one process can acquire or release a connection at a time, ensuring synchronized and safe access to the pool.

### **Conclusion:**
The use of semaphores in a ConnectionPool class effectively manages access to a limited resource pool, such as database connections. By limiting the number of concurrent processes that can acquire a connection, semaphores ensure that the system does not become overwhelmed by too many concurrent requests. This approach guarantees that only a specified number of processes can access the pool simultaneously, preventing race conditions and ensuring the safe and controlled use of resources.


## To run both at same time: 
`python main.py`
