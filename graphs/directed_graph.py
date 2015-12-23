class Directed_Graph:


    def __init__(self):
        self.graph_dict = {}

        
    def add_vertex(self, vertex):
        if vertex in self.graph_dict.keys():
            raise ValueError('trying to add same vertex multiple times')
        out_edges = {}
        in_edges = {}
        self.graph_dict[vertex] = (in_edges, out_edges)


    def add_edge(self, edge):
        (from_vertex, to_vertex, weight) = edge
        self.graph_dict[from_vertex][1][to_vertex] = weight
        self.graph_dict[to_vertex][0][from_vertex] = weight
        

    def list_vertices(self):
        return self.graph_dict.keys()
    

    def list_edges(self):
        edges = []
        for v in self.graph_dict.keys():
            edges += [(v, x, self.graph_dict[v][1][x]) for x in self.graph_dict[v][1].keys()]
        return edges
        
        
