class Directed_Graph:

    inward = 0
    outward = 1
    
    def __init__(self):
        self.graph_dict = {}

        
    def add_vertex(self, vertex):
        if vertex in self.graph_dict.keys():
            raise ValueError('trying to add same vertex multiple times')
        out_edges = {}
        in_edges = {}
        self.graph_dict[vertex] = (in_edges, out_edges)

    #overwrites previous edge if exists
    def add_edge(self, edge):
        (from_vertex, to_vertex, weight) = edge
        self.graph_dict[from_vertex][outward][to_vertex] = weight
        self.graph_dict[to_vertex][inward][from_vertex] = weight

    def list_vertices(self):
        return self.graph_dict.keys()

    def list_edges(self):
        edges = []
        for v in self.graph_dict.keys():
            edges += [(v, x, self.graph_dict[v][outward][x]) for x in self.graph_dict[v][outward].keys()]
        return edges
        
        
