import heapq

def knapsack_ucs(weights, profits, capacity):
    n = len(weights)

    
    pq = []
    heapq.heappush(pq, (0, 0, 0, 0))  

    visited = set()
    best_profit = 0

    while pq:
        cost, index, cur_weight, cur_profit = heapq.heappop(pq)

       
        best_profit = max(best_profit, cur_profit)

       
        if index == n:
            continue

      
        state = (index, cur_weight)
        if state in visited:
            continue
        visited.add(state)

        
        heapq.heappush(
            pq,
            (-cur_profit, index + 1, cur_weight, cur_profit)
        )

      
        if cur_weight + weights[index] <= capacity:
            heapq.heappush(
                pq,
                (-(cur_profit + profits[index]),
                 index + 1,
                 cur_weight + weights[index],
                 cur_profit + profits[index])
            )

    return best_profit


weights = [3, 4, 6, 5]
profits = [2, 3, 1, 4]
capacity = 8

print("Result:", knapsack_ucs(weights, profits, capacity))