from aoc2020 import graph
def test_dfs():
    adj = [[1,2], [2,3], [3], [3]]
    result = graph.search(adj, target=3, start=0, mode="dfs")
    assert len(result) == 3
    assert result == [3,2,0]
    result = graph.search(adj, target=3, start=0, mode="bfs")
    assert len(result) == 3
    assert result == [3,1,0]
    
