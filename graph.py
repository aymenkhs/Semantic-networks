

class SemanticNetwork:

    def __init__(self, network_name):

        self.network_name = network_name
        self.nodes = {}

    def __getitem__(self, index):
        return self.nodes[index]

    def __iter__(self):
        self.__keys = self.nodes.keys()
        self.__index_key = 0
        return self

    def __next__(self):
        if self.__index_key <= len(self.__keys):
            result = self.__index_key
            self.__index_key += 1
            return result
        else:
            raise StopIteration

    def add_nodes(self, nodes):
        for node in nodes:
            self.nodes[node["id"]] = Node(node["name"], node["id"])

    def add_connections(self, connections):
        for connection in connections:
            connection_source = Connection(connection["name"], self.nodes[connection["destination"]], connection["type"])
            connection_destination = Connection(connection["name"], self.nodes[connection["source"]], connection["type"])

            self.nodes[connection["source"]].connections_to.append(connection_source)
            self.nodes[connection["destination"]].connections_from.append(connection_destination)

    def id_name(self, name):
        for node in self.nodes.values():
            if name == node.name:
                return node.id
        return None


class Node:

    def __init__(self, name, id):

        self.name = name
        self.id = id

        self.connections_from = []
        self.connections_to = []

    def __str__(self):
        return "({}; {}; {})".format(self.name, self.connections_from, self.connections_to)

    def __repr__(self):
        return str(self)


class Connection:

    def __init__(self, name, node, type):
        self.name = name
        self.node = node
        self.type = type

    def __str__(self):
        return "({}/ {}/ {})".format(self.name, self.node.name, self.type)

    def __repr__(self):
        return str(self)
