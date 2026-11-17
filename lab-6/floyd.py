
def floydWarshall(graph):
    V = len(graph)

    for k in range(V):

        for i in range(V):

            for j in range(V):


                if ((graph[i][j] == -1 or 
                    graph[i][j] > (graph[i][k] + graph[k][j]))
                    and (graph[k][j] != -1 and graph[i][k] != -1)):
                    graph[i][j] = graph[i][k] + graph[k][j]

if __name__ == "__main__":
    graph = [
        [0,  2,  5,  7, -1, -1,  8, -1],
        [2,  0, -1, -1,  8, -1, -1, -1],
        [5, -1,  0, -1,  2,  4,  4, -1],
        [7, -1, -1,  0,  9,  5,  9, -1],
        [-1, 8,  2,  9,  0,  3, -1, -1],
        [-1, -1, 4,  5,  3,  0, -1,  1],
        [8, -1,  4,  9, -1, -1,  0,  6],
        [-1, -1, -1, -1, -1, 1,  6,  0]
    ]
    
    floydWarshall(graph)
    for i in range(len(graph)):
        for j in range(len(graph)):
            print(graph[i][j], end=" ")
        print()
