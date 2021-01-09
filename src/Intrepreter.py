from src.Node import Node
from src.Shape import Shape
from typing import List
import logging
from src.Graph import Graph


class Interpreter:
    """
    This module gets a collection of fuzzy elevated surface shapes and then builds a hierarchy (non-cyclical graph;tree)
    depending on the objects' fuzzyness and surfaces.
    """

    def interpret(self, shapes:List[Shape]):
        logging.info(f"Creating hierarchy. There are {len(shapes)} nodes to order")
        graph = Graph()

        for shape in shapes:
            # Make node
            node = Node(shape.id)
            logging.info(f"Computing Node relationship {shape.id+1} of {len(shapes)}")

            # Find other nodes node points to
            for graph_node in graph.nodes:
                graph_node_id = graph_node.identifier
                graph_node_shape = shapes[graph_node_id].shape
                node_shape = shape.shape
                # Test if the two shapes overlap and have therefore a dependent relationship
                if node_shape.colliderect(graph_node_shape):
                    # Test if One contains the other
                    if node_shape.contains(graph_node_shape):
                        # Graph node is in Node
                        node.point_to(graph_node_id)
                        graph_node.pointed_at(node.identifier)
                    elif graph_node_shape.contains(node_shape):
                        # Node is in Graph node
                        graph_node.point_to(node.identifier)
                        node.pointed_at(graph_node)
                    else:
                        # The two don't contain each other, but collide
                        graph_node.point_to(node.identifier)
                        graph_node.pointed_at(node.identifier)
                        node.point_to(graph_node_id)
                        node.pointed_at(graph_node_id)
                # There is no else case, since not overlapping nodes don't point to each other
            # Append Nodes to graph
            graph.add_node(node)
        logging.info(f"Created hierarchy!")

        return graph

    def determine_kind(self, graph, shapes, theme):
        for shape in shapes:
            shape.kind = theme.determine_kind(graph, shapes, shape)

