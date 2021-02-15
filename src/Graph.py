from src.Node import Node

class Graph:

    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_node(self, identifier) -> Node:
        return self.nodes[identifier]

    def get_levels(self):
        for node in self.nodes:
            pass