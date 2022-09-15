from itertools import permutations
from sys import maxsize
import time



# Firstly run bellman ford on the graph to check if there are any negative weight cycles,
# or return the shortest distances from the start to the other vertices.
# Then bellman ford will also be run from each of the bunny nodes in the graph to determine the
# lowest weight paths between bunnies. Then all of the paths between bunnies from the start
# will be checked to see the highest length bunny route (which ends at the exit) which 
# has sufficiently low weight.
# Dijkstra cannot be used since it does not work with negatively weighted graphs.


def bellamn_ford_shortest_dists(graph_matrix, start_node):
    V = len(graph_matrix)
    dists = [maxsize for i in range(V)]
    dists[start_node] = 0 # Distance from start to start is 0

    # For every iteration over every edge, this gives at least the shortest paths 
    # for all paths from the start length 1. Therefore at a maximum, there needs to
    # be |V| - 1 iterations over every edge, where |V| is the graph's number of
    # vertices. After, one more iteration is done to check if there are any negative
    # weight cycles.
    for v in range(V):
        prev_dists = dists[:] # This slicing is used to gain a shallow copy of the list.
        for x in range(V):
            for y in range(V):
                # The edge is from y -> x if the weight is the index [x][y] of the matrix.
                if x == y:
                    continue
                curr_weight = graph_matrix[y][x] + dists[y]
                if dists[x] > curr_weight:
                    if v == V - 1: # Checking for negative weight cycles
                        return False
                    dists[x] = curr_weight
        if prev_dists == dists:
            break
    return dists


def bunny_routes(V):
    # All of the longest routes will be returned first before the shorter ones.
    # The routes are represented by the index of the next bunny to visit.
    for num_buns in range(V-2, 0, -1):
        for route in permutations(range(1, V - 1), num_buns):
            yield route



def solution(times, time_limit):
    times_from_start = bellamn_ford_shortest_dists(times, 0)
    V = len(times)
    if not times_from_start:
        return range(V-2)
    # Get all the shortest times from each node (apart from the exit)
    shortest_times = [
        bellamn_ford_shortest_dists(times, node) for node in range(1, V-1) 
    ]
    shortest_times.insert(0, times_from_start)
    for route in bunny_routes(V):
        # This could be optimised to ignore routes that start with a sub-route which
        # has been discovered as ineligible however there is no need at the moment.
        # This would also have to account for negative weights which is quite a complication.
        route_sum = 0
        prev_node_num = 0
        for node_num in route:
            route_sum += shortest_times[prev_node_num][node_num]
            prev_node_num = node_num
        route_sum += shortest_times[prev_node_num][-1]
        if route_sum <= time_limit:
            return list(sorted([bun_idx - 1 for bun_idx in route]))


times = [
    [0, 2, 2, 2, -1], 
    [9, 0, 2, 2, -1], 
    [9, 3, 0, 2, -1], 
    [9, 3, 2, 0, -1], 
    [9, 3, 2, 2, 0]
]
start = time.time()
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))
print("---- %s seconds ----" %(time.time() - start))