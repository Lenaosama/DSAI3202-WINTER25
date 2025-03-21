from mpi4py import MPI
import numpy as np
import pandas as pd
import time

# Import your functions
from src.genetic_algorithm_trial import (
    distance_matrix,
)

num_nodes = distance_matrix.shape[0]

# Import your functions
from src.genetic_algorithms_functions import (
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

# ------------------------
# Main Execution Block
# ------------------------
if __name__ == "__main__":
    population_size = 100
    generations = 50

    population = generate_unique_population(population_size, num_nodes)

    if rank == 0:
        start_time = time.time()

    for gen in range(generations):
        fitness = parallel_fitness_evaluation(population, distance_matrix)

        if rank == 0:
            best_idx = np.argmin(fitness)
            print(f"Generation {gen}: Best calculate_fitness = {fitness[best_idx]}")

            selected = select_in_tournament(population, fitness, number_tournaments=population_size, tournament_size=3)

            new_population = [population[best_idx]]  # Elitism
            while len(new_population) < population_size:
                p1, p2 = np.random.choice(selected, 2, replace=False)
                child = order_crossover(p1, p2)
                new_population.append(mutate(child))

            population = new_population

        # Sync population across all ranks
        population = comm.bcast(population, root=0)

    if rank == 0:
        print(f"\n✅ GA completed in {time.time() - start_time:.2f} seconds.")
