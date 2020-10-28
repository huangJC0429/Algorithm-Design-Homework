import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

Inf = float('inf')

def Dijkstra(G, source):
    Q = []
    dist = {}
    prev = {}
    for i in range(len(G)):
        dist[i] = Inf
        Q.append(i)
        prev[i] = -1
    dist[source] = 0
    while len(Q) != 0:
        print(sorted(dist.items(), key=lambda kv: (kv[1], kv[0])))
        x = sorted(dist.items(), key=lambda kv: (kv[1], kv[0]))
        for xx in x:
            if xx[0] in Q:
                u = Q.pop(Q.index(xx[0]))
                break

        for v in range(len(G[u, :])):
            if G[u, v] != 0:
                alt = dist[u] + G[u, v]
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev


if __name__ == '__main__':

    # 索引用来查找哪个点对于哪个地铁站
    L = ["犀浦", "韦家碾", "石油大学", "一品天下", "火车北站", "驷马桥", "万盛",
         "文化宫", "中医大省医院", "骡马市", "市二医院", "槐树店", "西河", "天府广场",
         "春熙路", "省体育馆", "成都东客站", "太平园", "火车南站", "龙泉驿", "双流西站",
         "双流机场2航站楼", "天府三街"]
    node = [i for i in range(23)]
    print(node)
    G = nx.Graph()
    G.add_nodes_from(node)
    G.add_edge(0, 3, weight=8)
    G.add_edge(1, 4, weight=2)
    G.add_edge(2, 5, weight=12)
    G.add_edge(3, 4, weight=6)
    G.add_edge(4, 5, weight=1)
    G.add_edge(3, 7, weight=2)
    G.add_edge(3, 8, weight=3)
    G.add_edge(4, 9, weight=3)
    G.add_edge(5, 10, weight=4)
    G.add_edge(5, 11, weight=7)
    G.add_edge(6, 7, weight=13)
    G.add_edge(7, 8, weight=3)
    G.add_edge(8, 9, weight=2)
    G.add_edge(9, 10, weight=2)
    G.add_edge(10, 11, weight=4)
    G.add_edge(11, 12, weight=5)
    G.add_edge(7, 17, weight=4)
    G.add_edge(8, 13, weight=3)
    G.add_edge(9, 13, weight=1)
    G.add_edge(13, 14, weight=1)
    G.add_edge(13, 15, weight=3)
    G.add_edge(10, 14, weight=1)
    G.add_edge(14, 15, weight=3)
    G.add_edge(14, 16, weight=6)
    G.add_edge(11, 16, weight=2)
    G.add_edge(15, 17, weight=4)
    G.add_edge(15, 18, weight=3)
    G.add_edge(16, 19, weight=10)
    G.add_edge(17, 20, weight=11)
    G.add_edge(17, 21, weight=5)
    G.add_edge(17, 18, weight=3)
    G.add_edge(18, 22, weight=6)
    G.add_edge(18, 16, weight=6)

    a = np.array(nx.adjacency_matrix(G).todense())
    print(a)
    nx.draw_networkx(G)
    plt.show()
    dist, prev = Dijkstra(a, 2)
    print(dist)
    for x in range(len(dist)):
        print("从石油大学到", L[x], "最短的路径是", dist[x],"站")
    # print(prev)
    print("--------------以下是溯源，从西南石油大学到天府三街的具体最短路径为----------------")
    # 以下代码是溯源，从西南石油大学到天府三街的具体最短路径
    root = []
    end = 22
    while end != -1:
        root.append(end)
        end = prev[end]
    root.reverse()
    for a in root:
        print(L[a])