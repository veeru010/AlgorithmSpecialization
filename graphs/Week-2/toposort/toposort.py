#Uses python3

import sys




def dfs(adj, used, order, x):
    used[x] = True

    for node in adj[x]:
        if len(adj[node]) == 0 and used[node] is False:
            used[node] = True
            order.insert(0,node)
        elif used[node] is False:
            dfs(adj,used,order,node)
    order.insert(0,x)


def toposort(adj):
    used = [False for _ in range(len(adj))]
    order = []
    
    for i in range(len(adj)):
        if used[i] is False:
            dfs(adj,used,order,i)

    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

