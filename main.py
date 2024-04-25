from collections import deque
from heapq import heappush, heappop 


def shortest_shortest_path(graph, source):
  pq = [(0.0, 0, source)]  
  visited = set()
  results = {vertex: (float('infinity'), 0) for vertex in   graph}
  results[source] = (0.0, 0) 

  while pq:
    distance, edge_count, vertex = heappop(pq)
    if vertex in visited:
        continue
    visited.add(vertex)

    for neighbor, weight in graph.get(vertex, []):
        if neighbor not in visited:
            new_distance = distance + weight
            new_edge_count = edge_count + 1

            if new_distance < results.get(neighbor, (float('infinity'), 0))[0] or \
               (new_distance == results.get(neighbor, (float('infinity'), 0))[0] and        new_edge_count < results.get(neighbor, (float('infinity'), 0))[1]):
              results[neighbor] = (new_distance, new_edge_count)
              heappush(pq, (new_distance, new_edge_count, neighbor))

    return results
    

    
    
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
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  path = []
  current = destination
  while current is not None:
    path.append(current)
    current = parents.get(current)
  path.reverse()
  return ' -> '.join(path[:-1])  # exclude the destination node itself

