import time
from multiprocessing import Process, Semaphore, Manager

# ConnectionPool class to manage database connections
class ConnectionPool:
    def __init__(self, max_connections):
        self.max_connections = max_connections
        self.semaphore = Semaphore(max_connections)  # Semaphore to limit connections
        self.available_connections = Manager().list(range(max_connections))  # Shared list of connections

    def get_connection(self):
        self.semaphore.acquire()  # Wait until a connection is available
        connection = self.available_connections.pop(0)  # Get the first available connection
        print(f"Process {Process().name} acquired connection {connection}")
        return connection

    def release_connection(self, connection):
        self.available_connections.append(connection)  # Add the connection back to the pool
        self.semaphore.release()  # Release the semaphore
        print(f"Process {Process().name} released connection {connection}")

# Function to simulate a process accessing the database
def access_database(pool):
    connection = pool.get_connection()  # Get a connection
    time.sleep(2)  # Simulate work
    pool.release_connection(connection)  # Release the connection

# Main script
if __name__ == "__main__":
    # Configuration
    POOL_SIZE = 3  # Number of available connections
    NUM_PROCESSES = 10  # Number of processes trying to access the database

    # Create a connection pool
    pool = ConnectionPool(POOL_SIZE)

    # Create a list to hold process objects
    processes = []

    # Start processes
    for i in range(NUM_PROCESSES):
        p = Process(target=access_database, args=(pool,))
        p.start()
        processes.append(p)

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes completed.")
