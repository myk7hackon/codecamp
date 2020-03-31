def dfs(node, graph, visited):
    if not visited[node]:
        print(node, end=" ")
        visited[node] = True
        for i in graph[node]:
            dfs(i, graph, visited)


def bfs(node, graph, bfs_graph, visited, prev=(), level=0):
    # print(node,"  ",prev)
    prev = list(prev)
    level = level + 1
    if not visited[node]:
        if not bfs_graph:
            bfs_graph.append(node)
            visited[node] = True
        prev.append(node)
        start_index = len(bfs_graph)
        for i in graph[node]:
            if not visited[i]:
                if i == 9:
                    prev.append(9)
                    print("distance is ", level, "  ", prev)
                bfs_graph.append(i)
            # print(bfs_graph)
        for i in range(start_index, len(bfs_graph)):
            bfs(bfs_graph[i], graph, bfs_graph, visited, tuple(prev), level)

    return bfs_graph


def component(visited, graph, component_count):
    for node in range(len(graph)):
        if not visited[node]:
            component_count = component_count + 1
            # print(component_count)
            dfs(node, graph, visited)
            print()
    return component_count


final_ans = []
mas_len = 1024


def dungeon_test(dungeon, row, col, visited, level, lengths, prev=(), bfs_graph=[]):
    prev = list(prev)
    level = level + 1
    if visited[row][col] != "VISITED":
        if not bfs_graph:
            bfs_graph.append([row, col])
        visited[row][col] = "VISITED"
        prev.append([row, col])
        start_index = len(bfs_graph)
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (
                    row + i >= 0
                    and row + i < len(dungeon)
                    and col + j >= 0
                    and col + j < len(dungeon[0])
                ):
                    if dungeon[row][col] == "E":
                        print(prev)

                    if (
                        dungeon[row + i][col + j] != "#"
                        and visited[row + i][col + j] == "NOT VISITED"
                    ):
                        bfs_graph.append([row + i, col + j])
                        visited[row + i][col + j] = "IN TRANSITION"
                        # print(row + i, "  ", col + j)
                        if lengths[row + i][col + j] > level:
                            lengths[row + i][col + j] = level
        for i in range(start_index, len(bfs_graph)):
            dungeon_test(
                dungeon,
                bfs_graph[i][0],
                bfs_graph[i][1],
                visited,
                level,
                lengths,
                tuple(prev),
            )
        print(lengths)


graph = [[1, 2], [3], [4], [5, 6], [7, 8, 9], [], [], [], [], [], [10]]

dungeon = [
    [".", ".", ".", "#", ".", ".", "."],
    [".", "#", ".", ".", ".", "#", "."],
    [".", "#", ".", ".", ".", ".", "."],
    [".", ".", "#", "#", ".", ".", "."],
    ["#", ".", "#", "E", ".", "#", "."],
]

visited = [False for i in range(len(graph))]

# component = [-1 for i in range(len(graph))]

if __name__ == "__main__":
    print("starting DFS")
    dfs(0, graph, visited)
    print("starting BFS")
    bfs_graph = []
    new_bfs = bfs(0, graph, bfs_graph, [False for i in range(len(graph))])
    print(bfs_graph)
    component_count = 0
    print(new_bfs)
    visited = [False for i in range(len(graph))]
    print("starting components")
    component_count = component(visited, graph, component_count)
    print("components are ", component_count)
    print("Dungeon")
    lengths = [[100 for i in range(len(dungeon[0]))] for j in range(len(dungeon))]
    visited = [
        ["NOT VISITED" for i in range(len(dungeon[0]))] for j in range(len(dungeon))
    ]

    # from pprint import pprint

    # pprint(lengths)
    dungeon_test(dungeon, 0, 0, visited, 0, lengths)
    # print(mas_len, "  path is  ", final_ans)
