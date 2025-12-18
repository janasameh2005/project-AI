import time
import random

W = 8
items = [
    {"name":"Item 1","weight":3,"profit":2},
    {"name":"Item 2","weight":3,"profit":4},
    {"name":"Item 3","weight":4,"profit":2},
    {"name":"Item 4","weight":2,"profit":3},
]
N = len(items)

def calculate_metrics(state):
    profit = 0
    weight = 0
    for i, included in enumerate(state):
        if included == 1:
            profit += items[i]["profit"]
            weight += items[i]["weight"]
    return profit, weight

def generate_random_initial_state():
    initial_state = [0] * N
    temp_w = 0
    shuffled_indices = list(range(N))
    random.shuffle(shuffled_indices)
    for i in shuffled_indices: 
        if random.random() < 0.6 and temp_w + items[i]["weight"] <= W:
             initial_state[i] = 1
             temp_w += items[i]["weight"]
             
    return initial_state

def get_neighbors(state, current_weight):
    neighbors = []
    for i in range(N):
        if state[i] == 0:
            new_weight = current_weight + items[i]["weight"]
            if new_weight <= W:
                new_state = state[:]
                new_state[i] = 1
                neighbors.append(new_state)
    for i in range(N):
        if state[i] == 1:
            new_state = state[:]
            new_state[i] = 0
            neighbors.append(new_state)
    unique_neighbors = [list(t) for t in set(tuple(i) for i in neighbors)]
    
    return unique_neighbors

def hill_climbing_knapsack():
    
    random.seed(time.time()) 
    start_time = time.time()
    nodes_expanded = 0
    
    current_state = generate_random_initial_state()
    current_profit, current_weight = calculate_metrics(current_state)
    
    best_state = current_state
    best_profit = current_profit
    
    memory_used_approx = len(current_state) * 4 + 2 * 8

    while True:
        nodes_expanded += 1
        neighbors = get_neighbors(current_state, current_weight)
        
        best_neighbor_state = None
        best_neighbor_profit = current_profit
        
        for neighbor_state in neighbors:
            neighbor_profit, neighbor_weight = calculate_metrics(neighbor_state)
          
            if neighbor_profit > best_neighbor_profit:
                best_neighbor_profit = neighbor_profit
                best_neighbor_state = neighbor_state
            
        if best_neighbor_state is None:
            break
      
        current_state = best_neighbor_state
        current_profit = best_neighbor_profit
        current_profit, current_weight = calculate_metrics(current_state)

        if current_profit > best_profit:
            best_state = current_state
            best_profit = current_profit
        
        memory_used_approx += len(current_state) * 4 + 2 * 8

    end_time = time.time()
    
    final_profit, final_weight = calculate_metrics(best_state)
    
    return (best_state, final_profit, final_weight), end_time - start_time, nodes_expanded, memory_used_approx

solution, exec_time, nodes_exp, mem_used = hill_climbing_knapsack()
selected_items = [items[i]["name"] for i,x in enumerate(solution[0]) if x==1]
total_weight = sum(items[i]["weight"] for i,x in enumerate(solution[0]) if x==1)
total_profit = solution[1]

print("Direct algorithm results for Hill Climbing with a realistic starting point ")
print("Selected Items:", selected_items)
print("Total Weight:", total_weight)
print("Total Profit:", total_profit)
print("Execution Time:", exec_time)
print("Nodes Expanded:", nodes_exp)
print("Memory Used (approx):", mem_used, "bytes")