import random
import time

weights = [3, 4, 6, 5]
profits = [2, 3, 1, 4]
capacity = 8
num_items = len(weights)

population_size = 6
generations = 30
mutation_probability = 0.1


def create_chromosome():
    return [random.randint(0, 1) for _ in range(num_items)]


def fitness(chromosome):
    total_weight = 0
    total_profit = 0
   
    for i in range(num_items):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_profit += profits[i]
 
    if total_weight > capacity:
        return 0
    return total_profit


def random_selection(population):
    return random.sample(population, 2)


def crossover(parent1, parent2):
    point = random.randint(1, num_items - 1)
    return (
        parent1[:point] + parent2[point:],
        parent2[:point] + parent1[point:]
    )


def mutation(chromosome):
    for i in range(num_items):
        if random.random() < mutation_probability:
            chromosome[i] = 1 - chromosome[i]


def genetic_knapsack_random():
    start_time = time.time()

    population = [create_chromosome() for _ in range(population_size)]
    nodes_expanded = 0

    for _ in range(generations):
        new_population = []

        nodes_expanded += len(population)

        while len(new_population) < population_size:
            parent1, parent2 = random_selection(population)
            child1, child2 = crossover(parent1, parent2)
            mutation(child1)
            mutation(child2)
            new_population.extend([child1, child2])

        population = new_population[:population_size]

    end_time = time.time()

    best = max(population, key=lambda x: fitness(x))

    memory_used = population_size * num_items * 4

    return best, fitness(best), end_time-start_time, nodes_expanded, memory_used

best, best_profit, exec_time, nodes, memory = genetic_knapsack_random()

print("\nBest Chromosome:", best)
print("Maximum Profit:", best_profit)

print("\nSelected Items:")
total_weight = 0
for i in range(num_items):
    if best[i] == 1:
        print(f"Item {i+1}  Weight={weights[i]}  Profit={profits[i]}")
        total_weight += weights[i]

print("\nTotal Weight:", total_weight)

print("\n-------------------------")
print("Execution Time:", exec_time)
print("Nodes Expanded:", nodes)
print("Memory Used (approx):", memory, "bytes")
