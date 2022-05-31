

class PropagationMarqueurs:

    def __init__(self, reseaux_semantique):
        self.reseaux_semantique = reseaux_semantique

    def solve_for_node(self, node_id1, node_id2):

        open_direction1 = [self.reseaux_semantique[node_id1]]
        open_direction2 = [self.reseaux_semantique[node_id2]]

        closed_direction1 = []
        closed_direction2 = []

        solution_found = False
        connecion_solution = None
        type = None

        while (len(open_direction1) != 0 or len(open_direction2) != 0) and not solution_found:

            try:
                node1 = open_direction1.pop()
            except IndexError as e:
                pass
            else:
                open_direction1 += [conection.node for conection in node1.connections_from if conection.name == "is a"]
                closed_direction1.append(node1)

            try:
                node2 = open_direction2.pop()
            except IndexError as e:
                pass
            else:
                open_direction2 = open_direction2 + [conection.node for conection in node2.connections_from if conection.name == "is a"]
                closed_direction2.append(node2)

            for node in open_direction1 + closed_direction1:
                for connection in node.connections_from:
                    if connection.node in open_direction2 + closed_direction2 and connection.name != "is a":
                        solution_found = True
                        connecion_solution = connection.name
                        type = 1

                for connection in node.connections_to:
                    if connection.node in open_direction2 + closed_direction2 and connection.name != "is a":
                        solution_found = True
                        connecion_solution = connection.name
                        type = 2

        return solution_found, connecion_solution, type
