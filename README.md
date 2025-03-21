# DSAI3202-WINTER25
Parallel and distributed computing repository for labs and assignments. Created on 14/1/2025 by Lena Swaileh.


# DSAI 3202 - Assignment 1: Navigating the City (Genetic Algorithm for Fleet Management)

## Overview
This project uses a **Genetic Algorithm (GA)** to optimize delivery routes for a fleet of vehicles in a city. The primary objective is to minimize the total distance traveled by all vehicles while ensuring that each delivery node in the city is visited exactly once by any vehicle. This solution utilizes **parallel computing** techniques to distribute the workload across multiple machines, improving efficiency, especially for large datasets.

The project includes the implementation of a genetic algorithm with **MPI4PY** for parallelization and distributed computing. The problem was first solved sequentially and then parallelized to improve performance. The solution is extended to handle multiple vehicles, and the algorithm is tested on both a small and a large city map.

## Objectives
- Implement a **genetic algorithm** to optimize the delivery routes.
- Minimize the total distance traveled by all vehicles in a fleet while visiting each delivery node exactly once.
- Parallelize the genetic algorithm using **MPI4PY** or **Celery** for efficient computation across multiple machines.
- Extend the solution to handle multiple vehicles and large-scale problems.

## Key Concepts
- **Genetic Algorithms (GAs)**: An optimization technique inspired by natural selection, where a population of solutions evolves over time using operators such as **selection**, **crossover**, and **mutation**.
- **Parallel Computing**: Distribution of the computation tasks (fitness evaluation, selection..) across multiple machines to speed up execution.
- **Fleet Management**: Optimizing the routes for a fleet of vehicles, ensuring each vehicle visits a subset of delivery nodes while minimizing the total distance traveled.

## Steps Taken
### 1. Genetic Algorithm Implementation
The genetic algorithm consists of the following components:
- **Fitness Function**: This function calculates the total distance of a proposed route. If any route is infeasible (a node is unreachable), a large negative penalty is returned.
- **Selection**: A **tournament selection** method was used, where individuals compete in tournaments, and the winner is selected for crossover.
- **Crossover**: The genetic material from two parent solutions is combined to create offspring. This was implemented with a uniform crossover method.
- **Mutation**: Random changes were introduced to the offspring’s genetic makeup to maintain diversity and prevent premature convergence.

### 2. Parallelization
The genetic algorithm was initially implemented sequentially and then parallelized using **MPI4PY**:
- **Fitness Evaluation**: The fitness calculation for each individual in the population was parallelized, enabling simultaneous evaluation of multiple individuals across different machines.
- **Selection**: Tournament selection was also parallelized to improve performance.

The parallelized version showed a significant improvement in execution time, especially when applied to larger dataset.

### 3. Large-Scale Problem
The problem was tested on both a **small city map** and a **large city map**. The **`city_distances_extended.csv`** file represents the extended city layout, containing 100 nodes and 4000 routes. The parallelized algorithm successfully handled the larger dataset within a feasible time frame better than the small city.
For example, in the small city, the best route had a total distance of -2115.0, while the larger city map resulted in a total distance of -2697.0 in the final generation.

## Answers:
### How would you add more cars to the problem?
- Divide the City into Regions: Split the city into regions, assigning each vehicle to a region. Each vehicle will optimize its route within its assigned region.
- Vehicle Assignment: Each vehicle will start and end its route at the depot. Assign nodes to vehicles either based on proximity or evenly divided across vehicles.
- Independent Optimization: Optimize each vehicle's route independently. The fitness function will evaluate each vehicle's route within its region, using crossover and mutation on individual vehicle populations.
- Minimizing Total Distance: After optimizing each vehicle’s route, minimize the total distance by adjusting routes across vehicles to ensure the combined distance is as low as possible.

## Results:
#### Just an example of the long output I got:
Best Solution: [0, 10, 7, 31, 23, 12, 9, 2, 21, 20, 29, 26, 24, 4, 3, 5, 16, 28, 18, 27, 8, 15, 19, 1, 11, 6, 22, 30, 25, 17, 13, 14]
Total Distance: -2115.0

## Performance Metrics
The execution time and fitness of the algorithm were measured:
Sequential Execution: The genetic algorithm ran for several generations to find the optimal route. For example, in Generation 0, the best fitness was -1796.0, and after several generations, the best fitness reached -2115.0.
Parallel Execution: Using MPI4PY, the performance improved with a faster execution time due to distributed fitness evaluation and selection processes. The parallelized version showed a substantial reduction in computation time when applied to the extended dataset.

## Conclusion
This project successfully implemented and parallelized a genetic algorithm to solve the fleet management problem, optimizing delivery routes in a city. The algorithm was extended to handle larger problems and multiple vehicles, with performance improvements achieved through parallelization. This solution demonstrates the power of genetic algorithms and parallel computing for solving optimization problems efficiently.

