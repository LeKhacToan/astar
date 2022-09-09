from typing import Optional
from type import WeightedGraph, Location, GridLocation
from queue import PriorityQueue
from grid_graph import GridWithWeights, reconstruct_path
# from draw import draw_grid, DIAGRAM1_WALLS


def heuristic(a: GridLocation, b: GridLocation) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict[Location, Optional[Location]] = {}
    cost_so_far: dict[Location, float] = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current: Location = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def search(start: GridLocation, goal: GridLocation):
    diagram = GridWithWeights(50, 20)
    came_from, cost_so_far = a_star_search(diagram, start, goal)
    path = reconstruct_path(came_from, start=start, goal=goal)
    res = []
    for item in path:
        x, y = item
        res.append({'x': x, 'y': y})
    return res


# diagram4 = GridWithWeights(50, 20)
# diagram4.walls = DIAGRAM1_WALLS
# start, goal = (1, 4), (25, 2)
# came_from, cost_so_far = a_star_search(diagram4, start, goal)
# draw_grid(diagram4, point_to=came_from, start=start, goal=goal)
# print()
# path = reconstruct_path(came_from, start=start, goal=goal)
# draw_grid(diagram4, path=path)
