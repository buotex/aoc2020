from typing import List, Tuple, Dict
from enum import Enum



class SearchDirection(str, Enum):
    dfs = "dfs"
    bfs = "bfs"


def search(adj: List, target: int, start: int, mode: SearchDirection):
    memory: List[Tuple[int, int]] = [(start, start)]
    visited = [False for _ in adj]
    parent = [i for i in range(len(adj))]
    while True:
        if mode == "dfs":
            current, prev = memory.pop()
        elif mode == "bfs":
            current, prev = memory.pop()
        visited[current] = True
        parent[current] = prev
        if current == target:
            break
        for neighbor in adj[current]:
            if not visited[neighbor]:
                n = (neighbor, current)
                if mode == "dfs":
                    memory.append(n)
                elif mode == "bfs":
                    memory.insert(0, n)
    result = []
    while True:
        result.append(current)
        if current == start:
            break
        current = parent[current]
        
    return result


def search_dict(adj: Dict, target = None, start=None, mode: SearchDirection="dfs", *,
                count_func = lambda x, y: x
                ):
    keys = [key for key in adj.keys()]
    if start is None:
        start = keys[0]

    visited = {key: 0 for key in adj.keys()}
    parent = {key: False for key in adj.keys()}
    for key, val in adj.items():
        for entry in val:
            entry = entry[1:]
            visited[entry] = False
            parent[entry] = False

    memory: List[Tuple] = [(start, start, 1)]

    while True:
        if len(memory) == 0:
            break
        if mode == "dfs":
            current, prev, current_count = memory.pop()
        elif mode == "bfs":
            current, prev, current_count = memory.pop()
        visited[current] += current_count
        if parent[current] == False:
            parent[current] = prev
        if current == target:
            break
        for neighbor in adj[current]:
            neighbor_count = neighbor[0]
            neighbor = neighbor[1:]
            #if not visited[neighbor]:
            n = (neighbor, current, count_func(current_count, neighbor_count))
            if mode == "dfs":
                memory.append(n)
            elif mode == "bfs":
                memory.insert(0, n)
    result = []
    while True:
        result.append(current)
        if current == start:
            break
        current = parent[current]
        
    visited = [(key, value) for key, value in visited.items() if value > 0]
    return result, visited

