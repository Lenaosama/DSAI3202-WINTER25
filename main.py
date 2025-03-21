from mpi4py import MPI
import numpy as np
import time
import pandas as pd

<<<<<<< HEAD
# Replace 'city_distances.csv' with your actual file path
distance_matrix = pd.read_csv("city_distances.csv", header=None).values


from src.genetic_algorithms_functions import (
=======
from src. genetic_algorithms_functions import (
>>>>>>> b2753c5 (check)
    calculate_fitness,
    generate_unique_population,
    select_in_tournament,
    order_crossover,
    mutate,
)


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def parallel_fitness_evaluation(population, distance_matrix):
    chunk_size = len(population) // size
    start = rank * chunk_size
    end = len(population) if rank == size - 1 else (rank + 1) * chunk_size
    local_population = population[start:end]

    local_fitness = np.array([calculate_fitness(ind, distance_matrix) for ind in local_population])

    all_fitness = None
    if rank == 0:
        all_fitness = np.empty(len(population), dtype=np.float64)

    comm.Gather(local_fitness, all_fitness, root=0)

    return all_fitness if rank == 0 else None


# -----------------------------
# MAIN EXECUTION BLOCK
# -----------------------------
if __name__ == "__main__":
    num_nodes = len(distance_matrix)
    population_size = 100
    generations = 50

    population = generate_unique_population(population_size, num_nodes)

    if rank == 0:
        start_time = time.time()

    for gen in range(generations):
        fitness = parallel_fitness_evaluation(population, distance_matrix)

        if rank == 0:
            best_idx = np.argmin(fitness)  # Minimize total_distance (since it's negative)
            print(f"Generation {gen}: Best calculate_fitness = {fitness[best_idx]}")

            # ✅ Add logic for selection, crossover, and mutation
            selected = select_in_tournament(population, fitness, number_tournaments=population_size, tournament_size=3)

            new_population = [selected[0]]  # Elitism: keep best
            while len(new_population) < population_size:
                parents = np.random.choice(selected, 2, replace=False)
                child = order_crossover(parents[0], parents[1])
                mutated_child = mutate(child)
                new_population.append(mutated_child)

            population = new_population

        # Broadcast the new population to all processes
        population = comm.bcast(population, root=0)

    if rank == 0:
        duration = time.time() - start_time
        print(f"Parallel fitness evaluation took {duration:.2f} seconds.")
