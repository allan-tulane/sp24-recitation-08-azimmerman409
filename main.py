from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    distances = {vertex: (float('infinity'), 0) for vertex in graph}
    distances[source] = (0, 0)
    pq = [(0, 0, source)]

    while pq:
        current_distance, edges, current_vertex = heappop(pq)
        if current_distance > distances[current_vertex][0]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            edge_count = edges + 1
            if distance < distances[neighbor][0] or (distance == distances[neighbor][0] and edge_count < distances[neighbor][1]):
                distances[neighbor] = (distance, edge_count)
                heappush(pq, (distance, edge_count, neighbor))

    return distances

def bfs_path(graph, source):
    parents = {source: None}
    queue = deque([source])

    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in parents:
                parents[neighbor] = vertex
                queue.append(neighbor)

    return parents



def get_sample_graph():
  return {'s': [('a', 1), ('b', 1)],
          'a': [('b', 1)],
          'b': [('c', 1)],
          'c': [('a', 1), ('d', 1)],
          'd': []
         }


def get_path(parents, destination):
    path = []
    current = destination
    while current is not None:
        path.append(current)
        current = parents.get(current)
    path.reverse()
    return ' -> '.join(path[:-1])  # exclude the destination node itself

