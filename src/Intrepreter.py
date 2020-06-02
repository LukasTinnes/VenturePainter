from src.Node import Node


class Interpreter:
    """
    This module gets a collection of fuzzy elevated surface shapes and then builds a hierarchy (non-cyclical graph;tree)
    depending on the objects' fuzzyness and surfaces.
    """

    def __init__(self):
        pass

    def interpret(self, background, shapes):
        graph = [Node(hash(background))]
        for shape in shapes:
            node = Node(hash(shape))
            for graph_node in graph:
                # If background then just point background to object and break
                if hash(graph_node) == hash(background):
                    graph_node.point_to(node.get_identifier())
                    continue
                else:
                    node_shape = shapes[hash(node)]
                    node_bbox = node_shape.get_bounding_box()
                    graph_node_shape = shapes[hash(graph_node)]
                    graph_node_bbox = graph_node_shape.get_bounding_box()
                    # Case overlapping
                    # Todo overlap method doesnt work, problem in engine
                    if node_bbox.overlaps(node_bbox, graph_node_bbox):
                        # Case A in B
                        if node_bbox.overlaps_completely(graph_node_bbox):
                            # B points to A
                            graph_node.point_to(node.get_identifier())
                        else:
                            # A points to B and B points to A
                            graph_node.point_to(node.get_identifier())
                            node.point_to(graph_node.get_identifier())
            # Else no pointers, lastly append node to graph
            graph.append(node)
        return graph
