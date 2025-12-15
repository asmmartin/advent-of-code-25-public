"""https://adventofcode.com/2025/day/08"""

import heapq
import sys
from collections import defaultdict, deque
from functools import cache
from itertools import combinations
from time import perf_counter
from typing import Generic, TypeVar

type Coords = tuple[int, int, int]
type Connection = tuple[float, tuple[Coords, Coords]]
T = TypeVar("T")


def read_coords(text: str) -> tuple[Coords, ...]:
    coords: list[Coords] = []
    for line in text.splitlines():
        c = line.split(",")
        coords.append((int(c[0]), int(c[1]), int(c[2])))
    return tuple(coords)


def compute_distance(a: Coords, b: Coords) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


@cache
def get_possible_connections(coords: tuple[Coords, ...]) -> tuple[Connection, ...]:
    pairs = combinations(coords, 2)
    return tuple(sorted([(compute_distance(*p), p) for p in pairs]))


def count_close_circuit_junctions(
    coords: tuple[Coords, ...], connections: int
) -> list[int]:
    edges = get_possible_connections(coords)[:connections]

    # Adjacency list
    adj = defaultdict(list)
    for _, (u, v) in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    circuits = []

    for box in coords:
        if box not in visited:
            # DFS
            queue = deque([box])
            circuit = []
            visited.add(box)

            while queue:
                node = queue.popleft()
                circuit.append(node)
                for neighbour in adj[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            circuits.append(circuit)

    return sorted([len(c) for c in circuits], reverse=True)


def connect_all_boxes(coords: tuple[Coords, ...]) -> list[Connection]:
    # I can use either:
    #   Kruskal Algorithm: https://www.youtube.com/watch?v=8HeLu8wuLqo
    #   Prim's Algorithim: https://www.youtube.com/watch?v=EHRqQBlZAtU
    # Prim's is easier to implement, but Kruskal is faster (already sorted)

    # return connect_all_boxes_prims(coords)
    return connect_all_boxes_kruskals(coords)


def connect_all_boxes_prims(coords: tuple[Coords, ...]) -> list[Connection]:
    #   Prim's Algorithim: https://www.youtube.com/watch?v=EHRqQBlZAtU
    connections: list[Connection] = []

    edges = get_possible_connections(coords)

    # Graph as adjacency list
    graph = defaultdict(list[tuple[float, Coords]])
    for w, (u, v) in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    queue: list[Connection] = []
    visited = set()

    visited.add(coords[0])
    for distance, neighbour in graph[coords[0]]:
        heapq.heappush(queue, (distance, (coords[0], neighbour)))

    while queue:
        connection = heapq.heappop(queue)
        v = connection[1][1]
        if v in visited:
            continue
        visited.add(v)
        connections.append(connection)
        for distance, neighbour in graph[v]:
            if neighbour not in visited:
                heapq.heappush(queue, (distance, (v, neighbour)))

    return connections


def connect_all_boxes_kruskals(coords: tuple[Coords, ...]) -> list[Connection]:
    #   Kruskal Algorithm: https://www.youtube.com/watch?v=8HeLu8wuLqo
    connections: list[Connection] = []

    edges = get_possible_connections(coords)  # Already sorted

    disjoint_set = DisjointSet(coords)
    for connection in edges:
        root_u = disjoint_set.find(connection[1][0])
        root_v = disjoint_set.find(connection[1][1])

        if root_u != root_v:
            connections.append(connection)
            disjoint_set.union(root_u, root_v)

    return connections


class DisjointSet(Generic[T]):
    def __init__(self, vertices: tuple[T, ...]) -> None:
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, vertex: T) -> T:
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, root1: T, root2: T):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root2] > self.rank[root1]:
            self.parent[root1] = root2
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def main(input_text: str):
    start = perf_counter()

    # Part 1
    solution_1 = None
    coords = read_coords(input_text)
    count = count_close_circuit_junctions(coords, 1000)
    solution_1 = count[0] * count[1] * count[2]

    part_1_time = perf_counter() - start

    # Part 2
    solution_2 = None
    connections = sorted(connect_all_boxes(coords))
    solution_2 = connections[-1][1][0][0] * connections[-1][1][1][0]

    total_time = perf_counter() - start

    # Print solutions
    print(f"Solution part 1: {solution_1} ({part_1_time:.6f} seconds)")
    print(f"Solution part 2: {solution_2} ({total_time - part_1_time:.6f} seconds)")

    print(f"Complete day took {total_time:.6f} seconds")


if __name__ == "__main__":
    INPUT_TEXT = sys.stdin.read()
    main(INPUT_TEXT)
