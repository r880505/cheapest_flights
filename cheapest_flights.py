import heapq
from collections import defaultdict

def find_cheapest_flight(flights, src, dst, max_stops):
    if src == dst:
        return 0, f"{src}"

    flight_graph = defaultdict(list)
    for flight in flights:
        origin, destination, price = flight["from"], flight["to"], flight["price"]
        flight_graph[origin].append((destination, price))

    cost_table = defaultdict(lambda: [float("inf")] * (max_stops + 2))
    cost_table[src][0] = 0

    min_heap = [(0, src, 0, f"{src}")]

    while min_heap:
        current_cost, city, stops, path = heapq.heappop(min_heap)

        if city == dst:
            return current_cost, path

        if stops <= max_stops:
            for neighbor, price in flight_graph[city]:
                new_cost = current_cost + price
                new_path = f"{path} - {price} -> {neighbor}"
                
                if new_cost < cost_table[neighbor][stops + 1]:
                    cost_table[neighbor][stops + 1] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor, stops + 1, new_path))

    return -1, "No valid route found"
