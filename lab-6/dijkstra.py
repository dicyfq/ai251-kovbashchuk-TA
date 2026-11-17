import heapq


def dijkstra(graph, start):
    dist = {node: float("inf") for node in graph}
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue  # stale entry, a shorter path was already found
        for neighbor, weight in graph[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return dist


graph = {
    1: [(2, 2), (3, 5), (4, 7), (7, 8)],
    2: [(1, 2), (5, 8)],
    3: [(1, 5), (5, 2), (6, 4), (7, 4)],
    4: [(1, 7), (5, 9), (6, 5), (7, 9)],
    5: [(2, 8), (3, 2), (4, 9), (6, 3)],
    6: [(3, 4), (4, 5), (5, 3), (8, 1)],
    7: [(1, 8), (3, 4), (4, 9), (8, 6)],
    8: [(6, 1), (7, 6)],
}

for node, d in dijkstra(graph, 1).items():
    print(f"1 -> {node}: {d}")
