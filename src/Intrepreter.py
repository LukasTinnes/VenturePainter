from src.Node import Node


class Interpreter:
    """
    This module gets a collection of fuzzy elevated surface shapes and then builds a hierarchy (non-cyclical graph;tree),
    depending on the objects' fuzzyness and surfaces.
    """

    def __init__(self):
        pass

    def interpret(self, background, shapes):
        graph = [Node(hash(background))]
        for shape in shapes:
            node = Node(hash(shape))
            for graph_node in graph:
                node_shape = shapes[hash(node)]
                node_bbox = node_shape.get_bounding_box()
                graph_node_shape = shapes[hash(graph_node)]
                graph_node_bbox = graph_node_shape.get_bounding_box()
                if node_bbox.overlaps(node_bbox, graph_node_bbox):
                    if node_bbox.overlaps_completely(graph_node_bbox):
                        pass


            graph.append(node)
