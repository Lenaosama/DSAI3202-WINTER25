from mpi4py import MPI
import numpy as np
import pandas as pd
import time
import random  # Required for random.sample

# ... (imports and MPI setup)

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

            selected = select_in_tournament(population, fitness, number_tournaments=population_size, tournament_size=3)

            new_population = [population[best_idx]]  # Elitism
            if len(selected) >= 2:
                while len(new_population) < population_size:
                    p1, p2 = random.sample(selected, 2)
                    child = order_crossover(p1, p2)
                    new_population.append(mutate(child))
            else:
                new_population = generate_unique_population(population_size, num_nodes)

            population = new_population

        population = comm.bcast(population, root=0)

    if rank == 0:
        print(f"\nGA completed in {time.time() - start_time:.2f} seconds.")
