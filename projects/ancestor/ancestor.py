
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:

            self.vertices[v1].add(v2)

        else:
            raise IndexError("That vertex does not exist")


# def earliest_ancestor(ancestors, starting_node):

#     graph = Graph()

#     for pair in ancestors:
#         graph.add_vertex(pair[0])
#         graph.add_vertex(pair[1])

#         # add edges in reverse because we are going upstream
#         graph.add_edge(pair[1], pair[0])

#     queue = Queue()
#     queue.enqueue([starting_node])

#     longest_path = 1
#     earliest_ancestor = -1

#     while queue.size() > 0:
#         path = queue.dequeue()
#         vertex = path[-1]

#         if (len(path) >= longest_path and vertex < earliest_ancestor) or (len(path) > longest_path):
#             earliest_ancestor = vertex
#             longest_path = len(path)

#         edges = graph.vertices[vertex]
#         for edge in edges:
#             updated_path = path.copy()
#             updated_path.append(edge)
#             queue.enqueue(updated_path)

#     return earliest_ancestor


def earliest_ancestor(ancestors, starting_node):
    parents = []
    chilren = []
    for (parent, child) in ancestors:
        parents.append(parent)
        chilren.append(child)

    if starting_node not in chilren:
        return -1

    parent = starting_node

    q = Queue()
    q.enqueue(parent)

    while q.size() > 0:
        vertex = q.dequeue()

        smallest = None
        for (i, j) in ancestors:
            if vertex == j:
                smallest = i
                break

        for (grandparent, parent) in ancestors:
            if parent == vertex:
                if grandparent <= smallest:
                    q.enqueue(grandparent)
    return vertex
