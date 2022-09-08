from typing import Protocol, TypeVar
from queue import Queue
from type import Location, Graph


class SimpleGraph:
    def __init__(self):
        self.edges: dict[Location, list[Location]] = {}
    
    def neighbors(self, id: Location) -> list[Location]:
        return self.edges[id]


example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'E'],
    'E': ['F'],
    'F': [],
}


def breadth_first_search(graph: Graph, start: Location):
    # print out what we find
    frontier = Queue()
    frontier.put(start)
    reached: dict[Location, bool] = {}
    reached[start] = True
    
    while not frontier.empty():
        current: Location = frontier.get()
        print("  Visiting %s" % current)
        for next in graph.neighbors(current):
            if next not in reached:
                frontier.put(next)
                reached[next] = True

print('Reachable from A:')
breadth_first_search(example_graph, 'A')
print('Reachable from E:')
breadth_first_search(example_graph, 'E')

