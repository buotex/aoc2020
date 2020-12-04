from typing import List, Tuple
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

