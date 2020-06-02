class Node:
    """
    A node in a graph
    """

    def __init__(self, identifier):
        """
        :param identifier: Identifier is hash of given Shape Object
        """
        self.identifier = identifier
        self.pointer = []

    def get_identifier(self):
        return self.identifier

    def point_to(self, identifier):
        self.pointer.append(identifier)

    def search_for(self, identifier):
        return self.__search_for(identifier, [])

    def __search_for(self, identifier, exclude):
        if self.identifier == identifier:
            return self
        else:
            for node in self.pointer:
                if not hash(node) in exclude:
                    exclude.append(hash(node))
                    ret = node.__search_for(identifier, exclude)
                    if ret is not None:
                        return ret

    def __hash__(self):
        return self.identifier
