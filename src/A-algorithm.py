import time

W = 8
items = [
    {"name": "Item 1", "weight": 3, "profit": 2},
    {"name": "Item 2", "weight": 3, "profit": 4},
    {"name": "Item 3", "weight": 4, "profit": 2},
    {"name": "Item 4", "weight": 2, "profit": 3},
]

#  Heuristic function
def heuristic(state, remaining):
    h = 0
    candidates = []
    for i, t in enumerate(state):
        if t == 0:
            ratio = items[i]["profit"] / items[i]["weight"]
            candidates.append((ratio, items[i]["weight"], items[i]["profit"]))
    #sorting
    candidates.sort(reverse=True)
    for ratio, weight, profit in candidates:
        if weight <= remaining:
            h += profit
            remaining -= weight
       
    return h

# A* Search 
def a_star_knapsack():
    start = time.time()
    pq = [([0]*len(items), 0, 0)]  # (state, profit, weight)
    best = None
    visited = set()
    total_nodes = 0  
    unique_nodes = 0  

    while pq:
        #sort top f(n)
        pq.sort(key=lambda x: x[1] + heuristic(x[0], W - x[2]), reverse=True)
        state, g, w = pq.pop(0)
        total_nodes += 1

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))
        unique_nodes += 1

       
        if best is None or g > best[1]:
            best = (state, g, w)

    
        for i in range(len(items)):
            if state[i] == 0 and w + items[i]["weight"] <= W:
                new_state = state.copy()
                new_state[i] = 1
                pq.append((new_state, g + items[i]["profit"], w + items[i]["weight"]))

    end = time.time()

 
    memory_used = sum(len(state)*4 + 2*8 for state, g, w in pq) + len(best[0])*4 + 2*8

    return best, end-start, total_nodes, unique_nodes, memory_used

#execution
solution, exec_time, total_nodes, unique_nodes, mem_used = a_star_knapsack()

selected_items = [items[i]["name"] for i,x in enumerate(solution[0]) if x==1]
total_weight = sum(items[i]["weight"] for i,x in enumerate(solution[0]) if x==1)
total_profit = solution[1]

print("Selected Items:", selected_items)
print("Total Weight:", total_weight)
print("Total Profit:", total_profit)
print("Execution Time:", exec_time)
print("Total Nodes Expanded:", total_nodes)
print("Unique Nodes Expanded:", unique_nodes)
print("Memory Used (approx):", mem_used, "bytes")