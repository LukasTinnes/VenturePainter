from .Theme import Theme
from src.Graph import Graph


class NeighborTheme(Theme):

    def __init__(self):
        super().__init__()

    def prepare(self, graph, shapes):
        pass

    def determine_kind(self, graph : Graph, shapes, shape):
        if graph.get_node(shape.id).has_edges():
            if graph.get_node(shape.id).has_mutual_edge():
                return "mutual"
            else:
                return "one_direction"
        else:
            return "no_edges"
