import subprocess
import os

def main():
    # Define the directory where the scripts are located
    src_dir = os.path.join(os.getcwd(), 'src')

    print("\n=== Running Process Synchronization with Semaphores ===")
    subprocess.run(["python", os.path.join(src_dir, "Process_synchronization_with_semaphores.py")])

    print("\n=== Running Square Program ===")
    subprocess.run(["python3", os.path.join(src_dir, "Square_program.py")])

if __name__ == "__main__":
    main()
