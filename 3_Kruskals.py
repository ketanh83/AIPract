class Node:
    def __init__(self):
        self.parent = -1
        self.rank = 0


class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def find(v, dsuf):
    if dsuf[v].parent == -1:
        return v
    # Path compression
    dsuf[v].parent = find(dsuf[v].parent, dsuf)
    return dsuf[v].parent


def union_op(fromP, toP, dsuf):
    # Union by rank
    if dsuf[fromP].rank > dsuf[toP].rank:
        dsuf[toP].parent = fromP
        dsuf[fromP].rank += 1
    elif dsuf[fromP].rank < dsuf[toP].rank:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1
    else:
        dsuf[fromP].parent = toP
        dsuf[toP].rank += 1


def kruskals(edge_list, V):
    dsuf = [Node() for _ in range(V)]
    edge_list.sort(key=lambda edge: edge.wt)  # Sort by weight

    mst = []
    i = 0  # Tracks the number of edges in MST
    j = 0  # Index for iterating over sorted edges

    while i < (V - 1) and j < len(edge_list):
        edge = edge_list[j]
        fromP = find(edge.src, dsuf)
        toP = find(edge.dest, dsuf)

        if fromP != toP:
            union_op(fromP, toP, dsuf)
            mst.append(edge)
            i += 1
        j += 1

    return mst


def print_mst(mst):
    for edge in mst:
        print(f"\nsrc : {edge.src}\ndest : {edge.dest}\nwt : {edge.wt}\n")


def main():
    E = int(input("Enter the number of edges: "))
    V = int(input("Enter the number of vertices: "))

    edge_list = []
    for _ in range(E):
        s, d, w = map(int, input("Enter source, destination, and weight: ").split())
        edge_list.append(Edge(s, d, w))

    mst = kruskals(edge_list, V)
    print_mst(mst)


if __name__ == "__main__":
    main()

