class Node:
    """
    A node in a graph
    """

    def __init__(self, identifier):
        """
        :param identifier: Identifier is hash of given Shape Object
        """
        self.identifier = identifier
        self.outgoing_pointers = []
        self.incoming_pointers = []

    def get_identifier(self):
        return self.identifier

    def point_to(self, identifier):
        """
        Points to Node with the given identifier.
        :param identifier:
        :return:
        """
        self.incoming_pointers.append(identifier)

    def pointed_at(self, identifier):
        self.outgoing_pointers.append(identifier)

    def has_edges(self):
        return len(self.incoming_pointers) > 0 or len(self.outgoing_pointers) > 0

    def has_mutual_edge(self):
        for in_edge in self.incoming_pointers:
            if in_edge in self.outgoing_pointers:
                return True
        return False

    def search_for(self, identifier):
        return self.__search_for(identifier, [])

    def __search_for(self, identifier, exclude):
        if self.identifier == identifier:
            return self
        else:
            for node in self.incoming_pointers:
                if not hash(node) in exclude:
                    exclude.append(hash(node))
                    ret = node.__search_for(identifier, exclude)
                    if ret is not None:
                        return ret

    def __hash__(self):
        return self.identifier
