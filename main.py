from mpi4py import MPI
import numpy as np
import pandas as pd
import time
import random

# Switch to extended city map
distance_matrix = pd.read_csv("data/city_distances_extended.csv", header=None).values
num_nodes = distance_matrix.shape[0]

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


if __name__ == "__main__":
    population_size = 100
    generations = 200

    population = generate_unique_population(population_size, num_nodes)

    if rank == 0:
        start_time = time.time()

    for gen in range(generations):
        fitness = parallel_fitness_evaluation(population, distance_matrix)

        if rank == 0:
            best_idx = np.argmin(fitness)
            best_fitness = fitness[best_idx]
            print(f"Generation {gen}: Best calculate_fitness = {best_fitness}")

            if gen == generations - 1:
                print("Best Solution:", population[best_idx])
                print("Total Distance:", -best_fitness)
                break

            if np.isinf(fitness).all():
                print(f"Generation {gen}: All individuals infeasible. Regenerating population.")
                population = generate_unique_population(population_size, num_nodes)
                continue

            selected = select_in_tournament(population, fitness, number_tournaments=population_size, tournament_size=3)

            new_population = [population[best_idx]]  # Elitism

            while len(new_population) < population_size:
                p1, p2 = random.sample(selected, 2)
                child = order_crossover(p1, p2)
                child = mutate(child)

                # Validate and fix child
                child = [gene for gene in child if gene < num_nodes]
                if len(set(child)) != num_nodes:
                    child = [0] + list(np.random.permutation(np.arange(1, num_nodes)))

                new_population.append(child)

            population = new_population

        population = comm.bcast(population, root=0)

    if rank == 0:
        print(f"\nGA completed in {time.time() - start_time:.2f} seconds.")
